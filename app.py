#Librerias necesarias para el arranque del programa
import streamlit as st
from src.processor import carga, filtros_aplicados, ArchivoSinDatos, ColumnaNumericaNoEncontrada, identificar_tipo_columna
import src.processor as processor
from src.visualizer import renderizador_graficos
from src.utils import exportar_csv, exportar_excel
from src.languages import t, LANGUAGES

#If you see a lot of errors by "Error Lens", i dont know why is happening, i asked to gemini 3 pro, and just give a identation solution that didnt work lol. but the app is working


#page configuration
st.set_page_config(page_title="DataRefine", layout="wide")

# --- language selector ---
if 'language' not in st.session_state:
    st.session_state.language = 'es'

# Usamos columnas para poner el selector a la derecha
_, col_lang = st.columns([4, 1])

with col_lang:
    with st.popover("🌐 " + t("language_label")):
        idioma_sel = st.radio(
            "Seleccionar idioma",
            options=["es", "en", "pt"],
            format_func=lambda x: {"es": "🇪🇸 Español", "en": "🇬🇧 English", "pt": "🇧🇷 Português"}.get(x),
            label_visibility="collapsed",
            key="lang_radio"
        )
        if idioma_sel != st.session_state.language:
            st.session_state.language = idioma_sel
            st.rerun()

#titulo de la pagina
st.title(t("app_title"))
st.write(t("app_desc"))

archivo_subido = st.file_uploader(t("upload"), type=["csv", "xlsx"])

#Widget para subi el archivo
if archivo_subido:
    try:
        #carga el archivo subido
        if 'df' not in st.session_state or st.session_state.get('file_name') != archivo_subido.name:
            st.session_state['df'] = carga(archivo_subido)
            st.session_state['file_name'] = archivo_subido.name
            st.success(t("upload_success"))
        
        df = st.session_state['df']

        with st.sidebar:
            st.markdown("---")
            st.subheader(t("cleaning_tools"))
            
            # Usamos un expander para que no ocupe mucho espacio si no se usa
            with st.expander(t("cleaning_tools")):
                
                # 1. Limpieza de Nombres de Columnas (Rápido y útil)
                if st.button(t("normalize_cols")):
                    # Aplicamos la función probada
                    df_limpio = processor.limpiar_nombres_columnas(st.session_state['df'])
                    st.session_state['df'] = df_limpio
                    st.success(t("normalize_success"))
                    st.rerun() # Recargamos para que la UI vea los nuevos nombres

                st.markdown(f"### {t('null_mgmt')}")
                
                # Selector de estrategia
                opcion_nulos = st.selectbox(
                    t("null_action_label"),
                    [t("null_option_1"), t("null_option_2"), t("null_option_3"), t("null_option_4")]
                )
                
                valor_constante = None
                if opcion_nulos == t("null_option_4"):
                    valor_constante = st.text_input(t("input_fill_value"), value="0")

                if st.button(t("apply_nulls")):
                    # Mapeo de UI a argumentos de función
                    estrategia_map = {
                        t("null_option_1"): "eliminar",
                        t("null_option_2"): "rellenar_media",
                        t("null_option_3"): "rellenar_moda",
                        t("null_option_4"): "rellenar_constante"
                    }
                    estrategia = estrategia_map[opcion_nulos]
                    
                    # Llamamos a nuestra función probada
                    df_actualizado = processor.gestionar_nulos(
                        st.session_state['df'], 
                        estrategia=estrategia, 
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
                                        
        # --- SECCIÓN DE FILTROS CON SESSION STATE ---
        st.sidebar.header(t("global_filters"))

        # Inicializar estado si no existe
        if "columna_sel" not in st.session_state:
            st.session_state.columna_sel = df.columns[0]
        if "valor_sel" not in st.session_state:
            st.session_state.valor_sel = "Todos"

        # Callbacks para manejar cambios
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

        # Identificar tipo de columna para referencia (se puede expandir la lógica de filtros luego)
        tipo_col = identificar_tipo_columna(df, columna_filtrada)
        st.sidebar.caption(f"{t('data_type')}: {tipo_col.capitalize()}")

        opciones = ["Todos"] + df[columna_filtrada].unique().tolist()
        
        # Asegurarse de que el valor seleccionado existe en las opciones actuales
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
        # --------------------------------------------

        st.subheader(t("visualization"))

        eje_y = st.selectbox(t("select_y_axis"), df.select_dtypes(include=["number"]).columns)

        fig = renderizador_graficos(df_filtrado, columna_filtrada, eje_y, "Barras")
        st.plotly_chart(fig, width="stretch")
        
        st.divider()
        st.divider()
        st.subheader(t("editable_table"))
        st.info(t("edit_info"))

        #Dataframe final con correciones
        df_final = st.data_editor(df_filtrado)

        #mostrar metricas basicas en columnas
        # manejo de excepciones



        st.divider()

        st.subheader(t("download_data"))
        # Alerta
        st.warning(t("download_warning"))


        
        try:
            #Llamada a la Funcion para convertir el Dataframe editado a csv
            csv_nuevo = exportar_csv(df_final)
            
            #Llamada a la Funcion para convertir el Dataframe editado a excel
            excel_nuevo = exportar_excel(df_final)
            
            
            st.download_button(
            label=f"📈 {t('btn_download_csv')}",
            data=csv_nuevo,
            file_name="datos_editados.csv",
            mime="text/csv")
            

            
            #boton de descarga


        # Para descargar en Excel (.xlsx)
            st.download_button(
                label=f"📈 {t('btn_download_excel')}",
                data=excel_nuevo,
                file_name="datos_editados.xlsx",
                mime="application/vnd.ms-excel")
            
        except Exception as e:
            st.error(t("download_error", error=e))

    except ArchivoSinDatos as a:
        st.error(t("error_file_empty"))
        st.info(t("hint_file_empty"))

    except ColumnaNumericaNoEncontrada as c:
        st.error(t("error_no_numeric"))
        st.info(t("hint_no_numeric"))

       
    except Exception as e:
        st.error(t("save_error", error=e))
