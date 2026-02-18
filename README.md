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
  🌐 <a href="README_ES.md">Versión en Español</a> | <a href="https://data-pandas.streamlit.app/">Live Demo</a>
</p>

---

## 📸 Preview
![DataRefine Dashboard](assets/demo.gif) 

---

## 🛠 Project Overview
**DataRefine** is a modular web application built with **Python** and **Streamlit**. It solves the common friction of data cleaning by providing an intuitive interface for dataset standardization, null value management, and real-time interactive plotting.

### Key Capabilities:
* **Multi-format Support:** Seamlessly handles CSV and Excel (XLSX) files.
* **Automated Data Cleaning:** One-click text standardization and smart null-value imputation (Mean, Zero, or Drop).
* **Interactive Grid:** Direct cell editing powered by Streamlit's latest data editor components.
* **Dynamic Visuals:** Integrated **Plotly** engine for real-time, filter-responsive data visualization.
* **Professional Export:** Secure processed-data download in industry-standard CSV format.

## 🏗 Modular Architecture
Engineered with a focus on **Separation of Concerns (SoC)** to ensure scalability:
* `app.py`: UI orchestration and State Management.
* `logic/processor.py`: The core engine for data validation and Pandas-based transformations.
* `logic/visualizer.py`: Logic-layer for Plotly chart generation.
* `logic/utils.py`: Helper functions for file I/O and encoding.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pip

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/DataRefine.git](https://github.com/your-username/DataRefine.git)
   pip install -r requirements.txt
   streamlit run app.py
   ```

## 🎯 Target Use Case
DataRefine is tailored for marketing teams and data analysts who require rapid pre-processing of reports without the overhead of complex BI tools like PowerBI or Tableau.

## 🤝 Contributing & Feedback
As a Computer Engineer, I am constantly refining this tool. If you have suggestions regarding performance optimization or new features, feel free to open an Issue or a Pull Request.
