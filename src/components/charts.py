import streamlit as st
from src.languages import t
from src.visualizer import renderizador_graficos

def render_charts(df_filtrado, columna_filtrada):
    st.subheader(t("visualization"))

    eje_y = st.selectbox(t("select_y_axis"), df_filtrado.select_dtypes(include=["number"]).columns)

    fig = renderizador_graficos(df_filtrado, columna_filtrada, eje_y, "Barras")
    st.plotly_chart(fig, width="stretch")