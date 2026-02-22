<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<h1 align="center">DataRefine (MVP)</h1>

<p align="center">
  <strong>A high-performance data preprocessing and visualization engine.</strong><br />
  Designed for analysts who need to transform raw data into insights instantly.
</p>

<p align="center">
  <a href="README_ES.md">Versión en Español</a> | <a href="https://data-pandas.streamlit.app/">Live Demo</a>
</p>

---

## Preview
![DataRefine Dashboard](assets/demo.gif) 

---

## Project Overview
**DataRefine** is a modular web application built with **Python** and **Streamlit**. It solves the common friction of data cleaning by providing an intuitive interface for dataset standardization, null value management, and real-time interactive plotting.

### Key Capabilities:
* **Multi-format Support:** Seamlessly handles CSV and Excel (XLSX) files.
* **Automated Data Cleaning:** One-click text standardization and smart null-value imputation (Mean, Zero, or Drop).
* **Interactive Grid:** Direct cell editing powered by Streamlit's latest data editor components.
* **Dynamic Visuals:** Integrated **Plotly** engine for real-time, filter-responsive data visualization.
* **Professional Export:** Secure processed-data download in industry-standard CSV format.

## Modular Architecture
Engineered with a focus on **Separation of Concerns (SoC)** to ensure scalability:
* `app.py`: UI orchestration and State Management.
* `logic/processor.py`: The core engine for data validation and Pandas-based transformations.
* `logic/visualizer.py`: Logic-layer for Plotly chart generation.
* `logic/utils.py`: Helper functions for file I/O and encoding.
* `components/charts`: the components that shows the visualizations.
* `components/exports`: render and exports csv/excel funtions.
* `components/sidebar`: the sidebar with the cleaning and filtering functions.

## Roadmap: DataRefine (MVP Evolution)

This roadmap is designed to improve the robustness, analytical capability, and user experience of the application.

#### Phase 1: Robustness and User Experience (Short Term)
*Objective: Ensure the application is stable and user-friendly.*

- [x] **Advanced Error Handling**: Improve `try-except` blocks to provide specific messages (e.g., encoding errors in CSVs).
- [x] **Visual Feedback**: Add `st.spinner()` or progress bars during heavy operations (file loading, export).
- [x] **Type Validation**: Ensure numeric operations (like filling with mean) are not offered for text columns.
- [x] **Changes Preview**: Show a "Before and After" view (perhaps just the first 5 rows) when applying cleaning.

#### Phase 2: Deep Exploratory Analysis (Medium Term)
*Objective: Empower the user with more analytical tools.*

- [ ] **Statistical Summary**: Add a section displaying `df.describe()` with key metrics (count, mean, deviation, min/max).
- [ ] **More Charts**:
  - Line Chart (for time series).
  - Scatter Plot (to see correlation between two numeric variables).
  - Pie Chart (for categorical distributions).
  - Correlation Heatmap.
- [ ] **Duplicate Detection**: Button to identify and remove duplicate rows.
- [ ] **Type Conversion**: Allow the user to manually change a column from Text to Date or Text to Number.

#### Phase 3: Intelligence and Automation (Long Term)
*Objective: Key differentiator using AI or automation.*

- [ ] **Chat with your Data (PandasAI)**: Integrate an LLM so the user can ask "What was the total sales in March?" and get the answer.

- [ ] **Automatic Reports**: Generate a downloadable PDF with the analysis summary and generated charts.
- [ ] **Change History**: Implement an "Undo" system using `st.session_state` to save previous versions of the DataFrame.

#### Phase 4: Engineering and Deployment (Technical)
*Objective: Professional and scalable code.*

- [x] **Modularization**: Separate UI logic (`app.py`) into smaller components (e.g., `components/sidebar.py`, `components/charts.py`).
- [ ] **Testing**: Add unit tests (`pytest`) for `src/processor.py` functions.
- [ ] **Dockerization**: Create a `Dockerfile` to facilitate deployment on any server.
 (roadmap done by gemini 3 pro)

## Getting Started

### Prerequisites
- Python 3.11+
- uv (or Pip like you prefer)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/DataRefine.git](https://github.com/your-username/DataRefine.git)
   uv pip install -r requirements.txt
   uv add -r requirements.txt
   streamlit run app.py
   ```

## Target Use Case
DataRefine is tailored for marketing teams and data analysts who require rapid pre-processing of reports without the overhead of complex BI tools like PowerBI or Tableau.

## Contributing & Feedback
As a Computer Engineer, I am constantly refining this tool. If you have suggestions regarding performance optimization or new features, feel free to open an Issue or a Pull Request.
