import streamlit as st
from src.languages import t
from src.utils import exportar_csv, exportar_excel

def render_exports(df_final):
    st.subheader(t("download_data"))
    st.warning(t("download_warning"))
    
    try:
        with st.spinner(t("processing")):
            csv_nuevo = exportar_csv(df_final)
            excel_nuevo = exportar_excel(df_final)
        
        st.download_button(
            label=f"📈 {t('btn_download_csv')}",
            data=csv_nuevo,
            file_name="datos_editados.csv",
            mime="text/csv"
        )
        
        st.download_button(
            label=f"📈 {t('btn_download_excel')}",
            data=excel_nuevo,
            file_name="datos_editados.xlsx",
            mime="application/vnd.ms-excel"
        )
        
    except Exception as e:
        st.error(t("download_error", error=e))