import streamlit as st

# Diccionario principal con todos los idiomas
LANGUAGES = {
    "es": {
        # Generales
        "app_title": "DataRefine MVP",
        "app_desc": "Herramienta de limpieza y análisis de datos",
        "language_label": "Idioma",
        "upload": "Carga tu archivo CSV o Excel",
        "uploading": "Procesando archivo...",
        "upload_success": "Archivo cargado exitosamente.",
        "upload_error": "Error al cargar el archivo.",
        "processing": "Procesando...",
        "all_columns": "Todas las columnas",
        "select_col_nulls": "Selecciona columna(s)",
        
        # Limpieza
        "cleaning_tools": "🧹 Herramientas de Limpieza",
        "normalize_cols": "Normalizar Nombres de Columnas",
        "normalize_success": "¡Nombres limpios! (minúsculas, sin espacios ni tildes)",
        
        # Nulos
        "null_mgmt": "Gestión de Nulos",
        "null_action_label": "¿Qué hacer con los datos faltantes?",
        "null_option_1": "Eliminar filas con nulos",
        "null_option_2": "Rellenar con media (numérico)",
        "null_option_3": "Rellenar con moda",
        "null_option_4": "Rellenar con valor constante",
        "apply_nulls": "Aplicar Limpieza de Nulos",
        "success_nulls": "Acción realizada: {action}",
        "input_fill_value": "Valor para rellenar:",
        
        # Texto
        "text_std": "Estandarización de Texto",
        "select_col": "Columna a estandarizar",
        "all_cat_cols": "Todas las columnas categóricas",
        "format": "Formato",
        "format_title": "Titulo",
        "format_upper": "MAYUSCULAS",
        "format_lower": "minusculas",
        "remove_accents": "Quitar tildes/acentos",
        "apply_text": "Aplicar Formato de Texto",
        "success_text": "Texto estandarizado correctamente",
        
        # Descargas
        "btn_download_csv": "Descargar CSV",
        "btn_download_excel": "Descargar Excel",
        "no_data": "No hay datos para mostrar.",
        "download_data": "Descargar Datos",
        "download_warning": "⚠ **Sugerencia**: Te recomendamos hacer una copia de seguridad de tus datos antes de descargarlos.",
        "download_error": "Error al descargar los datos: {error}",
        "save_error": "Error al guardar los datos: {error}",

        # Filtros y Visualización
        "global_filters": "Filtros Globales",
        "select_filter_col": "Selecciona una columna para filtrar",
        "data_type": "Tipo de dato",
        "all_option": "Todos",
        "select_value": "Selecciona el valor",
        "reset_filters": "Restablecer Filtros",
        "visualization": "Visualización",
        "select_y_axis": "Selecciona el dato de eje Y",
        "editable_table": "Tabla Editable",
        "edit_info": "Puedes editar cualquier celda",

        # Errores / Excepciones
        "error_file_empty": "Error: El archivo está vacío.",
        "hint_file_empty": "Sugerencia: Revisa que el archivo contenga datos y no sea solo una fila de encabezados",
        "error_no_numeric": "Error: No se encontraron datos numéricos.",
        "hint_no_numeric": "Sugerencia: Revisa que el archivo contenga datos numéricos, de lo contrario las gráficas no estarán disponibles"
    },
    "en": {
        # General
        "app_title": "DataRefine MVP",
        "app_desc": "Data cleaning and analysis tool",
        "language_label": "Language",
        "upload": "Upload your CSV or Excel file",
        "uploading": "Processing file...",
        "upload_success": "File uploaded successfully.",
        "upload_error": "Error loading file.",
        "processing": "Processing...",
        "all_columns": "All columns",
        "select_col_nulls": "Select column(s)",
        
        # Cleaning
        "cleaning_tools": "🧹 Cleaning Tools",
        "normalize_cols": "Normalize Column Names",
        "normalize_success": "Names cleaned! (lowercase, no spaces or accents)",
        
        # Nulls
        "null_mgmt": "Null Management",
        "null_action_label": "What to do with missing data?",
        "null_option_1": "Remove rows with nulls",
        "null_option_2": "Fill with mean (numeric)",
        "null_option_3": "Fill with mode",
        "null_option_4": "Fill with constant value",
        "apply_nulls": "Apply Null Cleaning",
        "success_nulls": "Action completed: {action}",
        "input_fill_value": "Value to fill:",
        
        # Text
        "text_std": "Text Standardization",
        "select_col": "Column to standardize",
        "all_cat_cols": "All categorical columns",
        "format": "Format",
        "format_title": "Title",
        "format_upper": "UPPERCASE",
        "format_lower": "lowercase",
        "remove_accents": "Remove accents",
        "apply_text": "Apply Text Format",
        "success_text": "Text standardized successfully",
        
        # Downloads
        "btn_download_csv": "Download CSV",
        "btn_download_excel": "Download Excel",
        "no_data": "No data to display.",
        "download_data": "Download Data",
        "download_warning": "⚠ **Suggestion**: We recommend backing up your data before downloading.",
        "download_error": "Error downloading data: {error}",
        "save_error": "Error saving data: {error}",

        # Filters & Visualization
        "global_filters": "Global Filters",
        "select_filter_col": "Select a column to filter",
        "data_type": "Data type",
        "all_option": "All",
        "select_value": "Select value",
        "reset_filters": "Reset Filters",
        "visualization": "Visualization",
        "select_y_axis": "Select Y-axis data",
        "editable_table": "Editable Table",
        "edit_info": "You can edit any cell",

        # Errors / Exceptions
        "error_file_empty": "Error: The file is empty.",
        "hint_file_empty": "Suggestion: Check that the file contains data and is not just a header row",
        "error_no_numeric": "Error: No numeric data found.",
        "hint_no_numeric": "Suggestion: Check that the file contains numeric data, otherwise charts will not be available"
    },
    "pt": {
        # Geral
        "app_title": "DataRefine MVP",
        "app_desc": "Ferramenta de limpeza e análise de dados",
        "language_label": "Idioma",
        "upload": "Carregue seu arquivo CSV ou Excel",
        "uploading": "Processando arquivo...",
        "upload_success": "Arquivo carregado com sucesso.",
        "upload_error": "Erro ao carregar arquivo.",
        "processing": "Processando...",
        "all_columns": "Todas as colunas",
        "select_col_nulls": "Selecione coluna(s)",
        
        # Limpeza
        "cleaning_tools": "🧹 Ferramentas de Limpeza",
        "normalize_cols": "Normalizar Nomes de Colunas",
        "normalize_success": "Nomes limpos! (minúsculas, sem espaços ou acentos)",
        
        # Nulos
        "null_mgmt": "Gestão de Nulos",
        "null_action_label": "O que fazer com dados faltantes?",
        "null_option_1": "Remover linhas com nulos",
        "null_option_2": "Preencher com média (numérico)",
        "null_option_3": "Preencher com moda",
        "null_option_4": "Preencher com valor constante",
        "apply_nulls": "Aplicar Limpeza de Nulos",
        "success_nulls": "Ação realizada: {action}",
        "input_fill_value": "Valor para preencher:",
        
        # Texto
        "text_std": "Padronização de Texto",
        "select_col": "Coluna para padronizar",
        "all_cat_cols": "Todas as colunas categóricas",
        "format": "Formato",
        "format_title": "Título",
        "format_upper": "MAIÚSCULAS",
        "format_lower": "minúsculas",
        "remove_accents": "Remover acentos",
        "apply_text": "Aplicar Formato de Texto",
        "success_text": "Texto padronizado com sucesso",
        
        # Downloads
        "btn_download_csv": "Baixar CSV",
        "btn_download_excel": "Baixar Excel",
        "no_data": "Sem dados para exibir.",
        "download_data": "Baixar Dados",
        "download_warning": "⚠ **Sugestão**: Recomendamos fazer um backup dos seus dados antes de baixar.",
        "download_error": "Erro ao baixar dados: {error}",
        "save_error": "Erro ao salvar dados: {error}",

        # Filtros e Visualização
        "global_filters": "Filtros Globais",
        "select_filter_col": "Selecione uma coluna para filtrar",
        "data_type": "Tipo de dado",
        "all_option": "Todos",
        "select_value": "Selecione o valor",
        "reset_filters": "Redefinir Filtros",
        "visualization": "Visualização",
        "select_y_axis": "Selecione o dado do eixo Y",
        "editable_table": "Tabela Editável",
        "edit_info": "Você pode editar qualquer célula",

        # Erros / Exceções
        "error_file_empty": "Erro: O arquivo está vazio.",
        "hint_file_empty": "Sugestão: Verifique se o arquivo contém dados e não é apenas uma linha de cabeçalho",
        "error_no_numeric": "Erro: Nenhum dado numérico encontrado.",
        "hint_no_numeric": "Sugestão: Verifique se o arquivo contém dados numéricos, caso contrário, os gráficos não estarão disponíveis"
    }
}

def t(key, **kwargs):

    # Obtener idioma de session_state, por defecto 'es'
    lang = st.session_state.get('language', 'en')
    
    # Obtener el diccionario del idioma, si no existe, usar español
    lang_dict = LANGUAGES.get(lang, LANGUAGES['en'])
    
    # Obtener el texto, si la clave no existe, devolver la clave
    text = lang_dict.get(key, key)
    
    # Si hay argumentos (ej: {action}), formatear el string
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text