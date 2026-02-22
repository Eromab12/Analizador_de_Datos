#Librerias necesarias para el arranque del programa
import streamlit as st
from src.processor import carga, ArchivoSinDatos, ColumnaNumericaNoEncontrada
from src.languages import t, LANGUAGES
from src.components.sidebar import render_sidebar
from src.components.charts import render_charts
from src.components.exports import render_exports

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
            with st.spinner(t("uploading")):
                st.session_state['df'] = carga(archivo_subido)
                st.session_state['file_name'] = archivo_subido.name
                st.success(t("upload_success"))
        
        df = st.session_state['df']

        # 1. Renderizar Sidebar (Limpieza y Filtros)
        # Retorna el dataframe filtrado y la columna usada para filtrar
        df_filtrado, columna_filtrada = render_sidebar()

        # 2. Renderizar Gráficos
        render_charts(df_filtrado, columna_filtrada)
        
        st.divider()
        st.divider()
        st.subheader(t("editable_table"))
        st.info(t("edit_info"))

        # 3. Tabla Editable
        df_final = st.data_editor(df_filtrado)

        #mostrar metricas basicas en columnas
        # manejo de excepciones



        st.divider()
        
        # 4. Sección de Descargas
        render_exports(df_final)

    except ArchivoSinDatos as a:
        st.error(t("error_file_empty"))
        st.info(t("hint_file_empty"))

    except ColumnaNumericaNoEncontrada as c:
        st.error(t("error_no_numeric"))
        st.info(t("hint_no_numeric"))

       
    except Exception as e:
        st.error(t("save_error", error=e))
