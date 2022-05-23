import logging
from test import compare_schemas, get_schema, expand_nested
import pandas as pd
from utils import normalization, get_delimiter, get_encoding, \
    read_config, compare

url = r"C:\Users\pc\Downloads\email.csv"

config_url = r"C:\Users\pc\PycharmProjects\4th-p\conf.json"


def formatting(file_url, conf_url):
    df = pd.read_csv(file_url)
    conf_ext, conf_delimiter, conf_encoding, conf_columns, schema, \
    conf_nested, conf_dtypes = read_config(conf_url)
    file_ext = file_url[-4:]
    file_columns = df.columns
    file_delimiter = get_delimiter(file_url)
    file_encoding = get_encoding(file_url)

    #
    # TODO: Disassemble the function
    result = compare(conf_ext, file_ext, conf_delimiter,
                     file_delimiter, conf_encoding, file_encoding)

    if result:
        logging.info("CSV file has an acceptable format")

        df.drop_duplicates(inplace=True)

        logging.info("duplicated rows are dropped")
        try:
            nested_column = expand_nested(df)
            res = normalization(df, nested_column)

            logging.info("Data layers are normalized according to schema")
            conf_schema = get_schema(config_url, nested_column)
            compare_schemas(conf_schema, res)
        except Exception as e:
            return "last value should be dictionary"
        return res



formatting(url, config_url)
