import streamlit as st
from src.languages import t
import src.processor as processor
from src.processor import identificar_tipo_columna, filtros_aplicados

def render_sidebar():
    """
    Renderiza la barra lateral con herramientas de limpieza y filtros.
    Retorna:
        df_filtrado: DataFrame después de aplicar filtros.
        columna_filtrada: Nombre de la columna usada para filtrar.
    """
    df = st.session_state['df']
    
    with st.sidebar:
        st.markdown("---")
        st.subheader(t("cleaning_tools"))
        
        # Usamos un expander para que no ocupe mucho espacio si no se usa
        with st.expander(t("cleaning_tools")):
            
            # 1. Limpieza de Nombres de Columnas
            if st.button(t("normalize_cols")):
                with st.spinner(t("processing")):
                    df_limpio = processor.limpiar_nombres_columnas(st.session_state['df'])
                    st.session_state['df'] = df_limpio
                    st.success(t("normalize_success"))
                    st.rerun()

            st.markdown(f"### {t('null_mgmt')}")
            
            # Selector de columnas para nulos
            col_nulos_sel = st.selectbox(
                t("select_col_nulls"),
                options=[t("all_columns")] + list(st.session_state['df'].columns),
                key="null_col_selector"
            )

            # Filtrar opciones según el tipo de columna seleccionada
            opciones_disponibles = [t("null_option_1"), t("null_option_3"), t("null_option_4")]
            
            mostrar_media = False
            if col_nulos_sel == t("all_columns"):
                mostrar_media = True
            elif identificar_tipo_columna(st.session_state['df'], col_nulos_sel) == "numerico":
                mostrar_media = True
            
            if mostrar_media:
                opciones_disponibles.insert(1, t("null_option_2"))

            # Selector de estrategia
            opcion_nulos = st.selectbox(
                t("null_action_label"),
                opciones_disponibles
            )
            
            valor_constante = None
            if opcion_nulos == t("null_option_4"):
                valor_constante = st.text_input(t("input_fill_value"), value="0")

            if st.button(t("apply_nulls")):
                with st.spinner(t("processing")):
                    estrategia_map = {t("null_option_1"): "eliminar", t("null_option_2"): "rellenar_media", t("null_option_3"): "rellenar_moda", t("null_option_4"): "rellenar_constante"}
                    estrategia = estrategia_map[opcion_nulos]
                    
                    cols_target = None if col_nulos_sel == t("all_columns") else [col_nulos_sel]

                    df_actualizado = processor.gestionar_nulos(
                        st.session_state['df'], 
                        estrategia=estrategia, 
                        columnas=cols_target,
                        valor_relleno=valor_constante
                    )
                    st.session_state['df'] = df_actualizado
                    st.success(t("success_nulls", action=opcion_nulos))
                    st.rerun()

            st.markdown(f"### {t('text_std')}")
            
            col_texto = st.selectbox(
                t("select_col"),
                options=[t("all_cat_cols")] + list(st.session_state['df'].select_dtypes(include='object').columns)
            )
            
            formato = st.selectbox(t("format"), [t("format_title"), t("format_upper"), t("format_lower")])
            quitar_tildes = st.checkbox(t("remove_accents"), value=True)

            if st.button(t("apply_text")):
                with st.spinner(t("processing")):
                    target_cols = None if col_texto == t("all_cat_cols") else [col_texto]
                    formato_map = {t("format_title"): "titulo", t("format_upper"): "mayusculas", t("format_lower"): "minusculas"}
                    
                    df_actualizado = processor.estandarizar_texto(
                        st.session_state['df'],
                        columnas=target_cols,
                        formato=formato_map[formato],
                        quitar_tildes=quitar_tildes
                    )
                    st.session_state['df'] = df_actualizado
                    st.success(t("success_text"))
                    st.rerun()
            
            st.markdown(f"### {t('duplicates_mgmt')}")
            
            if st.button(t("remove_duplicates")):
                with st.spinner(t("processing")):
                    df_limpio, count = processor.eliminar_duplicados(st.session_state['df'])
                    st.session_state['df'] = df_limpio
                    if count > 0:
                        st.success(t("duplicates_success", count=count))
                    else:
                        st.info(t("no_duplicates"))
                    st.rerun()

            st.markdown(f"### {t('analysis_tools')}")
            
            st.checkbox(t("show_summary"), value=False, key="show_summary_stats")
                                    
        # --- SECCIÓN DE FILTROS ---
        st.sidebar.header(t("global_filters"))

        # Lógica de estado de filtros
        if "columna_sel" not in st.session_state:
            st.session_state.columna_sel = df.columns[0]
        if "valor_sel" not in st.session_state:
            st.session_state.valor_sel = "Todos"

        def reset_filtros():
            st.session_state.columna_sel = df.columns[0]
            st.session_state.valor_sel = "Todos"

        def al_cambiar_columna():
            st.session_state.valor_sel = "Todos"

        columna_filtrada = st.sidebar.selectbox(
            t("select_filter_col"), 
            df.columns, 
            key="columna_sel",
            on_change=al_cambiar_columna
        )

        tipo_col = identificar_tipo_columna(df, columna_filtrada)
        st.sidebar.caption(f"{t('data_type')}: {tipo_col.capitalize()}")

        opciones = ["Todos"] + df[columna_filtrada].unique().tolist()
        
        if st.session_state.valor_sel not in opciones:
            st.session_state.valor_sel = "Todos"

        seleccion = st.sidebar.selectbox(
            t("select_value"), 
            opciones, 
            key="valor_sel",
            format_func=lambda x: t("all_option") if x == "Todos" else x
        )

        st.sidebar.button(t("reset_filters"), on_click=reset_filtros)

        df_filtrado = filtros_aplicados(df, columna_filtrada, seleccion)
        
        return df_filtrado, columna_filtrada