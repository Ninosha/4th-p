import csv
import chardet
import pandas as pd


def read_config(config_url):
    conf_df = pd.read_json(config_url)
    conf_df = conf_df["file"]
    ext = conf_df["ext"]
    delimiter = conf_df["delimiter"]
    encoding = conf_df["encoding"]
    schema = pd.json_normalize(conf_df["schema"])
    drop_duplicates = conf_df["drop_duplicates"]

    return ext, delimiter, encoding, schema, drop_duplicates


def update_config_schema(schema, nested_column):
    schema.columns = schema.columns.str.replace(f'{nested_column}.', '')

    return True


def get_delimiter(url):
    with open(url, 'r') as csvfile:
        delimiter = csv.Sniffer().sniff(csvfile.readline()).delimiter

        return delimiter


def get_encoding(url):
    with open(url, 'rb') as csvfile:
        res = chardet.detect(csvfile.read())
        return res["encoding"]
