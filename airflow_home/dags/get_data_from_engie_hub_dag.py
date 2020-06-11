from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from formation_indus_ds_avancee.data_loading import get_data_from_csv

default_args = {
    'depends_on_past': False,
    'email_on_failure': ['isma@octo.com', 'lena@octo.com'],
    'retries': 0,
    'task_concurrency': 2,
}

dag = DAG(
    'data_generator',
    default_args=default_args,
    description='Get data every 2min from Engie hub',
    start_date=datetime(2020, 6, 10),
    schedule_interval=timedelta(minutes=2)
)

get_data = PythonOperator(task_id='get_data_from_csv',
                          python_callable=get_data_from_csv,
                          provide_context=False,
                          dag=dag)

get_data
