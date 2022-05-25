from format_data import formatting
import os
from google.cloud import storage
from insert_to_sql import to_sql

url = "/home/ninosha/Downloads/email.csv"

config_url = "conf.json"


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = url


def etl_job(request):
    """
    :param request:
    :return:
    """
    storage_client = storage.Client()
    bucket_name = os.environ.get("bucket_name")
    blobs = list(storage_client.list_blobs(bucket_name))
    for file in blobs:
        formatted_df = formatting(file, config_url)
        to_sql(formatted_df, host, database, user, password, port, filename)

    return {
        "message":
            "file was foramtted successfully and uploaded to postgres"
    }
