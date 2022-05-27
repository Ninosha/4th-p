gcloud functions deploy normalize_data \
    --project=cedar-heaven-349107 \
    --region=europe-west1 \
    --entry-point=etl_job \
    --memory=512MB \
    --runtime=python38 \
    --service-account=cedar-heaven-349107@appspot.gserviceaccount.com \
    --env-vars-file=./vars.yaml \
    --trigger-http \
    --timeout=540s