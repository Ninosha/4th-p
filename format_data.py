import logging

import pandas as pd
from utils import normalization, get_delimiter, get_encoding, \
    read_config, compare

url = "/home/ninosha/Downloads/email.csv"

config_url = "/home/ninosha/Desktop/projects/4th_project/cf/conf.json"


def formatting(file_url, conf_url):
    df = pd.read_csv(file_url)
    conf_ext, conf_delimiter, conf_encoding, conf_columns, schema, \
    conf_nested, conf_dtypes = read_config(conf_url)
    file_ext = file_url[-4:]
    file_columns = df.columns
    file_delimiter = get_delimiter(file_url)
    file_encoding = get_encoding(file_url)
    file_nested_cols = eval(df["Location"][0]).keys()
    file_dtypes = df.dtypes
    # del schema["Location"]
    # schema.update(conf_nested)
    schema_columns = schema.keys()
    df_columns = df.columns

    for column, col_type in schema.items():
        # TODO: Check this
        assert str(df[column].dtype) == col_type

    # TODO: Disassemble the function
    result = compare(conf_ext, file_ext, conf_delimiter,
                     file_delimiter
                     , conf_encoding, file_encoding, conf_columns,
                     file_columns, conf_nested.keys(), file_nested_cols,
                     conf_dtypes, file_dtypes)

    if result:
        logging.info("CSV file has an acceptable format")

        df.drop_duplicates(inplace=True)

        logging.info("duplicated rows are dropped")

        res = normalization(df)

        logging.info("Data layers are normalized according to schema")

        return res


formatting(url, config_url)
