# Project Documentation: DataRefine (MVP)

## Overview
DataRefine is an interactive web application built with Streamlit designed to facilitate the loading, cleaning, analysis, and export of data from Excel and CSV files. The goal is to allow non-technical users to perform basic data engineering tasks visually.

## Current System Capabilities

### 1. Internationalization (i18n)
- **Language Selector**: Dynamic support for Spanish (ES), English (EN), and Portuguese (PT).
- **Persistence**: The selected language is maintained during the session.
- **Interface**: Accessible selector via a Popover in the top right corner.

### 2. Data Ingestion
- **Supported Formats**: `.csv` and `.xlsx`.
- **Automatic Detection**: Immediate loading and conversion to Pandas DataFrame.

### 3. Cleaning Tools (Data Cleaning)
Located in the `Sidebar`, allowing quick transformations:
- **Column Normalization**: Converts column names to `snake_case` (lowercase and underscores) for easier handling.
- **Null Management**:
  - Remove rows with nulls.
  - Fill with mean (numeric).
  - Fill with mode (categorical).
  - Fill with a custom constant value.
- **Text Standardization**:
  - Formats: Title, Uppercase, Lowercase.
  - Character cleaning: Option to remove accents/diacritics.
  - Selection: Applicable to all text columns or a specific one.

### 4. Exploration and Filtering
- **Global Filters**:
  - Dynamic selection of column to filter.
  - Automatic detection of column data type.
  - Filtering by specific values or "All".
  - **Reset** button to quickly clear filters.

### 5. Visualization
- **Interactive Charts**: Rendering of bar charts using Plotly.
- **Configuration**: X-axis based on current filter, Y-axis selectable (numeric columns).

### 6. Editing and Export
- **Editable Table**: User can modify values directly in the cell (`st.data_editor`).
- **Dual Export**:
  - Download in **CSV** format.
  - Download in **Excel (.xlsx)** format.

## Tech Stack
- **Frontend/Backend**: Python + Streamlit.
- **Data Processing**: Pandas.
- **Visualization**: Plotly Express.
- **File Handling**: OpenPyXL (for Excel).