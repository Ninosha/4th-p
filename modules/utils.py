import csv
import chardet
import pandas as pd


def read_config(config_url):
    conf_df = pd.read_json(config_url)
    conf_df = conf_df["file"]
    ext = conf_df["ext"]
    schema = pd.json_normalize(conf_df["schema"])
    drop_duplicates = conf_df["drop_duplicates"]

    return ext, schema, drop_duplicates


def update_config_schema(schema, nested_column):
    schema.columns = schema.columns.str.replace(f'{nested_column}.', '')

    return True


def rename_columns(column):

    return column.replace(" ", "_").lower()
