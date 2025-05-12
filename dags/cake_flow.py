import os
import sys

from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.cake_pipeline import get_cake_page



dag = DAG(
    dag_id='cake_flow',
    default_args={
        "owner": "Medard tesla",
        "start_date": datetime(2025, 5, 10),
    },
    schedule=None,
    catchup=False
)

# Extraction

extract_data_from_cake_site = PythonOperator(
    task_id="extract_data_from_cake_site",
    python_callable=get_cake_page,
    op_kwargs={"url": "https://www.cuisine-libre.org/pouding-chomeur"},
    dag=dag
)

#Preprocessing

#write