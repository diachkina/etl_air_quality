# Air Quality ETL Pipeline

This is an ETL pipeline built with Apache Airflow for collecting, processing, and visualizing air quality data.

## 📋 Project Overview
The pipeline consists of the following stages:
1. **Extract**: Fetches air quality data for 10 cities in the Netherlands using the [World Air Quality API](https://aqicn.org).
2. **Transform**: Cleans, structures, and prepares the data for analysis.
3. **Load**: Stores the data in a SQLite database.
4. **Visualize**: Generates visualizations, including:
   - Bar chart of AQI for cities.
   - Forecast trends for PM2.5 in each city.
   - Heatmap showing correlations between air quality parameters.

## 🛠 Technologies Used
- **Apache Airflow**: Workflow orchestration and task scheduling.
- **Python**:
  - `pandas`: Data manipulation and cleaning.
  - `requests`: API interaction.
  - `matplotlib` & `seaborn`: Data visualization.
  - `sqlite3`: Lightweight relational database.
- **SQLite**: Local database to store air quality data.
- **Git**: Version control.

## 📁 Project Structure
- `dags/air_quality_etl_dag.py` - Airflow DAG defining the workflow.
- `dags/extract.py` - Fetches air quality data from the API.
- `dags/transform.py` - Cleans and structures the data.
- `dags/load.py` - Loads the data into SQLite database.
- `dags/plot.py` - Generates visualizations.

