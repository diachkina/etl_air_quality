from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from extract import extract_data
from transform import transform_data
from load import load_data
from plot import plot_all_graphs

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'air_quality_etl',
    default_args=default_args,
    description='ETL pipeline for air quality data with plots',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data,
    )

    plot_task = PythonOperator(
        task_id='plot',
        python_callable=plot_all_graphs,
    )

    extract_task >> transform_task >> load_task >> plot_task
