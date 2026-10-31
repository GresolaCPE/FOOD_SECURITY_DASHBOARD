# Global Food Security Dashboard

An interactive data visualization and analysis project developed for **CPE 031 – Data Visualization and Analysis**. This dashboard explores global food security through different indicators, including food prices, fertilizer costs, agricultural production, and food insecurity.

## Project Overview

The Global Food Security Dashboard aims to present food security data in an organized and interactive way. It allows users to explore trends, compare indicators, and identify possible relationships between different factors affecting global food security.

## Features

- **Overview** – Displays a general summary and key indicators of global food security.
- **Food Price Analysis** – Explores food price trends and changes.
- **Fertilizer Cost Analysis** – Presents fertilizer cost trends and comparisons.
- **Agricultural Production** – Visualizes agricultural production data.
- **Food Insecurity Analysis** – Examines food insecurity indicators.
- **Relationship Analysis** – Explores relationships between selected food security indicators.
- **Key Findings** – Highlights important observations from the dataset.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## Project Structure

```text
FOOD_SECURITY_DASHBOARD/
│
├── data/
│   ├── food_security_indicators.csv
│   └── food_security_panel.csv
│
├── .streamlit/
│   └── config.toml
│
├── main.py
├── data_preparation.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

Follow these steps to set up the project on your local computer.

### 1. Clone the Repository

Open your terminal or PowerShell and run:

```bash
git clone https://github.com/GresolaCPE/FOOD_SECURITY_DASHBOARD.git
```

### 2. Navigate to the Project Folder

```bash
cd FOOD_SECURITY_DASHBOARD
```

### 3. Create a Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python projects.

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 5. Install Required Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Dashboard

After completing the installation, make sure your virtual environment is activated and run:

```bash
streamlit run main.py
```

The dashboard will automatically open in your default web browser.

To stop the application, press `Ctrl + C` in the terminal.

## Course Information

**Course:** CPE 031 – Data Visualization and Analysis  
**Project Title:** Global Food Security Dashboard 

## Repository

[https://github.com/GresolaCPE/FOOD_SECURITY_DASHBOARD](https://github.com/GresolaCPE/FOOD_SECURITY_DASHBOARD)
