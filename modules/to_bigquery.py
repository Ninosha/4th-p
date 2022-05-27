
def to_bigquery(df, destination_table_name, gcp_project_name):
    df.to_gbq(
        destination_table=destination_table_name,
        project_id=gcp_project_name,
        if_exists="replace",
    )