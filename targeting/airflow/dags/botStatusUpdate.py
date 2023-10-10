from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.models.baseoperator import chain

from elasticsearch import Elasticsearch

es = Elasticsearch([{"host":"localhost", "port":9200}])


MAPPING = {
  "mapping": {
    "properties": {
      "client__clientId": {
        "type": "long"
      },
      "client__contacts__contactType": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "client__contacts__contactValue": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "client__fio": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "client__phones__phoneNumber": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
    }
  }
}



def test_func(**kwargs):
    print("heloooooooooooooooooooooooooooooooooooooooooooooooooooooooow")
    es.indices.create(index="test")

    return es.ping()





with DAG(
    "botUpdateStatus",
    schedule=timedelta(seconds=3600),
    start_date=datetime(2023, 1, 1), 
    catchup=False,
) as dag:

    test = PythonOperator(
        task_id="test",
        python_callable = test_func
    )

    
    chain(test)




