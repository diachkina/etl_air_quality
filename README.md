# Air Quality ETL Pipeline

This is an ETL pipeline built with Apache Airflow for collecting, processing, and visualizing air quality data.

## 📌 Project Structure
- `dags/air_quality_etl_dag.py` - Airflow DAG defining the workflow.
- `dags/extract.py` - Fetches air quality data from the API.
- `dags/transform.py` - Cleans and structures the data.
- `dags/load.py` - Loads the data into SQLite database.
- `dags/plot.py` - Generates visualizations.
