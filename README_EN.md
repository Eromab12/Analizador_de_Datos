🌐 Language / Idioma English Version | Versión en Español

# 📊 Data Analyzer Pro

A robust web application built with **Python** and **Streamlit** for loading, cleaning, and interactive visualization of datasets (CSV and Excel).

This project follows **modular architecture** principles, ensuring scalability and clean code maintenance.

## 🚀 Key Features
- **Versatile Loading**: Support for CSV and Excel files.
- **Automated Cleaning**: Tools for text standardization and missing value treatment (mean, removal, or zero-filling).
- **Live Editor**: Modify cells directly within the interface with instant updates.
- **Dynamic Visualization**: Interactive Plotly charts that respond to global filters in real-time.
- **Secure Export**: Download your processed data as a CSV file.

## 🏗️ Project Architecture
The system is decoupled into modules to separate business logic from the UI:
- `app.py`: Entry point and UI management (Streamlit).
- `logic/processor.py`: Core engine for processing, validation, and cleaning (Pandas).
- `logic/visualizer.py`: Generation of interactive charts (Plotly).
-`logic/utils.py`: Helper functions for exporting files

## 🛠️ Installation & Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

or you can use the online version
Dando click en el enlace [https://data-pandas.streamlit.app/] (Yeah I have to think better in the name 😂)

## 🎯 Target Audience
Ideal for data analysts and marketing teams who need to pre-process quick reports without relying on complex BI tools.

## Contribution

You can improve this application or even create a better one based on it.

If you have any suggestions or advice about the application or my way of doing it, feel free to let me know; that way, I will keep improving in this world of programming 🤓.
