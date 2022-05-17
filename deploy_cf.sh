gcloud functions deploy gcp_bq_crawler \
    --project=crawler-project-349107 \
    --region=europe-west1 \
    --entry-point=write_metadata_to_bucket \
    --memory=512MB \
    --runtime=python38 \
    --service-account=django-chained@crawler-project-349107.iam.gserviceaccount.com \
    --env-vars-file=./cf_variables.yaml \
    --trigger-http \
    --timeout=540s