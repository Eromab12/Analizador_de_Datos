🌐 Language / Idioma English Version | Versión en Español

# 📊 Data Analyzer Pro (MVP)

Una aplicación web robusta construida con **Python** y **Streamlit** para la carga, limpieza y visualización interactiva de datasets (CSV y Excel). 

Este proyecto fue diseñado siguiendo principios de **arquitectura modular**, permitiendo una fácil escalabilidad y mantenimiento.

## 🚀 Características
- **Carga Versátil**: Soporte para archivos CSV y Excel.
- **Limpieza Automática**: Herramientas para estandarización de texto y tratamiento de valores nulos (media, eliminación o ceros).
- **Editor en Vivo**: Modificación de celdas directamente en la interfaz.
- **Visualización Dinámica**: Gráficos interactivos con Plotly que se actualizan en tiempo real según los filtros aplicados.
- **Exportación Segura**: Descarga los datos procesados en formato CSV.

## 🏗️ Arquitectura del Proyecto
El sistema se divide en módulos para separar la lógica de negocio de la interfaz de usuario:
- `app.py`: Punto de entrada y gestión de la interfaz de usuario (Streamlit).
- `logic/processor.py`: Motor de procesamiento, validaciones y limpieza (Pandas).
- `logic/visualizer.py`: Generación de gráficos interactivos (Plotly).
- `logic/utils.py`: Funciones auxiliares de exportacion de archivos

## 🛠️ Instalación y Uso
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar la app: `streamlit run app.py`

## 🎯 Caso de Uso
Ideal para analistas de datos y equipos de marketing que necesitan pre-procesar reportes rápidos sin depender de herramientas complejas de BI.