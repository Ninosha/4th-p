import logging
import pandas as pd
from utils import read_config, update_config_schema, \
    get_delimiter, get_encoding
from main_funcs import expand_nested, compare_schemas, \
    extend_file, compare


def formatting(file_url, conf_url):
    conf_ext, conf_delimiter, conf_encoding, schema, drop_duplicates = \
        read_config(conf_url)

    file_ext = file_url[-4:]

    file_delimiter = get_delimiter(file_url)

    file_encoding = get_encoding(file_url)

    result = compare(conf_ext, file_ext, conf_delimiter,
                     file_delimiter, conf_encoding,
                     file_encoding)
    if result:
        logging.info("CSV file has an acceptable format")

        df = pd.read_csv(file_url)

        nested_column = expand_nested(df)

        logging.info("CSV data is extended")

        update_config_schema(schema, nested_column)

        logging.info("Configuration schema is updated")

        if drop_duplicates:
            df.drop_duplicates(inplace=True)

            logging.info("duplicated rows are dropped")

        extended_df = extend_file(df, nested_column)

        formatted_df = compare_schemas(schema, extended_df)

        logging.info("Data layers are normalized according to schema")

        print(formatted_df)
        return formatted_df

    else:
        message = "format is not acceptable"

        logging.info(message)

        return message
