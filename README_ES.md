Language / Idioma [English Version](README.md)| Versión en Español

# Data Analyzer Pro (MVP)

Una aplicación web robusta construida con **Python** y **Streamlit** para la carga, limpieza y visualización interactiva de datasets (CSV y Excel). 

Este proyecto fue diseñado siguiendo principios de **arquitectura modular**, permitiendo una fácil escalabilidad y mantenimiento.

## Características
- **Carga Versátil**: Soporte para archivos CSV y Excel.
- **Limpieza Automática**: Herramientas para estandarización de texto y tratamiento de valores nulos (media, eliminación o ceros).
- **Editor en Vivo**: Modificación de celdas directamente en la interfaz (Dataframe editable).
- **Visualización Dinámica**: Gráficos interactivos con Plotly que se actualizan en tiempo real según los filtros aplicados.
- **Exportación Segura**: Descarga los datos procesados en formato CSV.

## Arquitectura del Proyecto
El sistema se divide en módulos para separar la lógica de negocio de la interfaz de usuario:
- `app.py`: Punto de entrada y gestión de la interfaz de usuario (Streamlit).
- `logic/processor.py`: Motor de procesamiento, validaciones y limpieza (Pandas).
- `logic/visualizer.py`: Generación de gráficos interactivos (Plotly).
- `logic/utils.py`: Funciones auxiliares de exportacion de archivos


## Roadmap: DataRefine (Evolución del MVP)

Este roadmap está diseñado para mejorar la robustez, la capacidad analítica y la experiencia de usuario de la aplicación.

## Fase 1: Robustez y Experiencia de Usuario (Corto Plazo)
*Objetivo: Que la aplicación no falle y sea más amigable.*

- [x] **Manejo de Errores Avanzado**: Mejorar los bloques `try-except` para dar mensajes más específicos (ej. error de encoding en CSVs).
- [x] **Feedback Visual**: Agregar `st.spinner()` o barras de progreso durante operaciones pesadas (carga de archivos, exportación).
- [x] **Validación de Tipos**: Asegurar que las operaciones numéricas (como rellenar con la media) no se ofrezcan en columnas de texto.
- [x] **Preview de Cambios**: Mostrar una vista de "Antes y Después" (quizás solo las primeras 5 filas) al aplicar una limpieza.

## Fase 2: Análisis Exploratorio Profundo (Mediano Plazo)
*Objetivo: Dar más poder analítico al usuario.*

- [ ] **Resumen Estadístico**: Agregar una sección que muestre `df.describe()` con métricas clave (conteo, media, desviación, min/max).
- [ ] **Más Gráficos**:
  - Gráfico de Líneas (para series temporales).
  - Scatter Plot (para ver correlación entre dos variables numéricas).
  - Pie Chart (para distribuciones categóricas).
  - Heatmap de correlación.
- [ ] **Detección de Duplicados**: Botón para identificar y eliminar filas duplicadas.
- [ ] **Conversión de Tipos**: Permitir al usuario cambiar manualmente una columna de Texto a Fecha o de Texto a Número.

## Fase 3: Inteligencia y Automatización (Largo Plazo)
*Objetivo: Diferenciador clave mediante IA o automatización.*

- [ ] **Chat con tus Datos (PandasAI)**: Integrar un LLM para que el usuario pueda preguntar "¿Cuál fue la venta total en marzo?" y obtener la respuesta.
- [ ] **Reportes Automáticos**: Generar un PDF descargable con el resumen del análisis y los gráficos generados.
- [ ] **Historial de Cambios**: Implementar un sistema de "Deshacer" (Undo) usando `st.session_state` para guardar versiones anteriores del DataFrame.

## Fase 4: Ingeniería y Despliegue (Técnico)
*Objetivo: Código profesional y escalable.*

- [x] **Modularización**: Separar la lógica de la UI (`app.py`) en componentes más pequeños (ej. `components/sidebar.py`, `components/charts.py`).
- [ ] **Testing**: Añadir pruebas unitarias (`pytest`) para las funciones de `src/processor.py`.
- [ ] **Dockerización**: Crear un `Dockerfile` para facilitar el despliegue en cualquier servidor.


## Instalación y Uso
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar la app: `streamlit run app.py`

o pueden usar la versión online:

Dando click en el enlace [https://data-pandas.streamlit.app/]

## Caso de Uso
Ideal para analistas de datos y equipos de marketing que necesitan pre-procesar reportes rápidos sin depender de herramientas complejas de BI.
## Posibles mejoras
## Contribucion

Pueden mejorar esta aplicacion o incluso crear una mejor apartir de esta.

Si tienen alguna sugerencia o consejos acerca de la aplicacion, no duden en decirmelos de esa manera ire mejorando en este mundo de la programación 🤓.
