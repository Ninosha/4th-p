import os
from modules.format_data import formatting
from modules.to_bigquery import to_bigquery
from google.cloud import storage

CONFIG_URL = os.getenv("CONFIG_URL")
BUCKET_NAME = os.getenv("BUCKET_NAME")
TO_NORMALIZE_DIR = os.getenv("TO_NORMALIZE_DIR")
RAW_DIR = os.getenv("RAW_DIR")
DATASET_NAME = os.getenv("DATASET_NAME")


def etl_job(request):
    storage_client = storage.Client()
    prefix = TO_NORMALIZE_DIR
    blobs = list(storage_client.list_blobs(BUCKET_NAME,
                                           prefix=prefix))
    bucket = storage_client.get_bucket(BUCKET_NAME)

    for blob in blobs:
        blob_name = blob.name.replace(prefix, "")
        if blob_name:
            blob_url = f'gs://{BUCKET_NAME}/{prefix}{blob_name}'

            status, df = formatting(blob_url, CONFIG_URL)

            if status:
                new_dest = RAW_DIR + "/" + blob_name
                bucket.rename_blob(blob, new_dest)
                table_name = f"{DATASET_NAME}.{blob_name[:-4]}"
                to_bigquery(df, table_name, storage_client.project)

                return "success"

    return "not success"
