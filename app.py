#Librerias necesarias para el arranque del programa
import streamlit as st
from src.processor import carga, filtros_aplicados, ArchivoSinDatos, ColumnaNumericaNoEncontrada, identificar_tipo_columna
from src.visualizer import renderizador_graficos
from src.utils import exportar_csv, exportar_excel


        
#configuracion de la pagina
st.set_page_config(page_title="DataRefine", layout="wide")

#titulo de la pagina
st.title("DataRefine")
st.write("Sube tu archivo para visualizar un resumen automatico.")

archivo_subido = st.file_uploader("Elige un archivo a subir", type=["csv", "xlsx"])

#Widget para subi el archivo
if archivo_subido:
    try:
        #carga el archivo subido
        df = carga(archivo_subido)
        st.success("Archivo validado correctamente")

        # --- SECCIÓN DE FILTROS CON SESSION STATE ---
        st.sidebar.header("Filtros Globales")

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
            "Selecciona una columna para filtrar", 
            df.columns, 
            key="columna_sel",
            on_change=al_cambiar_columna
        )

        # Identificar tipo de columna para referencia (se puede expandir la lógica de filtros luego)
        tipo_col = identificar_tipo_columna(df, columna_filtrada)
        st.sidebar.caption(f"Tipo de dato: {tipo_col.capitalize()}")

        opciones = ["Todos"] + df[columna_filtrada].unique().tolist()
        
        # Asegurarse de que el valor seleccionado existe en las opciones actuales
        if st.session_state.valor_sel not in opciones:
            st.session_state.valor_sel = "Todos"

        seleccion = st.sidebar.selectbox(
            "Selecciona el valor", 
            opciones, 
            key="valor_sel"
        )

        st.sidebar.button("Restablecer Filtros", on_click=reset_filtros)

        df_filtrado = filtros_aplicados(df, columna_filtrada, seleccion)
        # --------------------------------------------

        st.subheader("Visualizacion")

        eje_y = st.selectbox("Selecciona el dato de eje Y", df.select_dtypes(include=["number"]).columns)

        fig = renderizador_graficos(df_filtrado, columna_filtrada, eje_y, "Barras")
        st.plotly_chart(fig, width="stretch")
        
        st.divider()
        st.divider()
        st.subheader("Tabla Editable")
        st.info("Puedes editar cualquier celda")

        #Dataframe final con correciones
        df_final = st.data_editor(df_filtrado)

        #mostrar metricas basicas en columnas
        # manejo de excepciones



        st.divider()

        st.subheader("Descargar Datos")
        # Alerta
        st.warning("⚠ **Sugerencia**: Te recomendamos hacer una copia de seguridad de tus datos antes de descargarlos.")


        
        try:
            #Llamada a la Funcion para convertir el Dataframe editado a csv
            csv_nuevo = exportar_csv(df_final)
            
            #Llamada a la Funcion para convertir el Dataframe editado a excel
            excel_nuevo = exportar_excel(df_final)
            
            
            st.download_button(
            label="📈 Descargar como CSV",
            data=csv_nuevo,
            file_name="datos_editados.csv",
            mime="text/csv")
            

            
            #boton de descarga


        # Para descargar en Excel (.xlsx)
            st.download_button(
                label="📈 Descargar como Excel",
                data=excel_nuevo,
                file_name="datos_editados.xlsx",
                mime="application/vnd.ms-excel")
            
        except Exception as e:
            st.error(f"Error al descargar los datos: {e}")

    except ArchivoSinDatos as a:
        st.error(f"Error: {a}")
        st.info("Sugerencia: Reivsa que el archivo contenga datos y no sea solo una fila de encabezados")

    except ColumnaNumericaNoEncontrada as c:
        st.error(f"Error: {c}")
        st.info("Sugerencia: Revisa que el archivo contenga datos numericos, de lo contrario las graficas no estaran disponibles")

       
    except Exception as e:
        st.error(f"Error al guardar los datos: {e}")
