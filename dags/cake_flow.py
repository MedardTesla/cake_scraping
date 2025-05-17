import os
import sys
import json


from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.cake_pipeline import get_list_recette, get_exist_recette, write_data
JSON_FILE_NAME = "data/recette.json"



dag = DAG(
    dag_id='cake_flow',
    default_args={
        "owner": "Medard tesla",
        "start_date": datetime(2025, 5, 10),
    },
    schedule=None,
    catchup=False
)



# charger donnée

read_exist_data = PythonOperator(
    task_id="read_exist_data",
    python_callable=get_exist_recette,
    op_kwargs={"_JSON_FILE_NAME":JSON_FILE_NAME},
    dag=dag
    

)

# Extraction

extract_data_from_cake_site = PythonOperator(
    task_id="extract_data_from_cake_site",
    python_callable=get_list_recette,
    op_kwargs={"url":"https://www.cuisine-libre.org/boulangerie-et-patisserie?mots%5B%5D=83&max=50"},
    dag=dag
)



    
#write

write_data_info_json_file = PythonOperator(
    task_id="write_data_info_json_file",
    python_callable=write_data,
    # op_kwargs={"JSON_FILE_NAME":"recette.json"},
    dag=dag
)

read_exist_data >> extract_data_from_cake_site >>  write_data_info_json_file

