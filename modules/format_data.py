import logging
import pandas as pd
from modules.utils import read_config, update_config_schema, rename_columns
from modules.main_funcs import expand_nested, compare_schemas, \
    extend_file, compare


def formatting(file_url, conf_url):
    conf_ext, schema, drop_duplicates = \
        read_config(conf_url)

    file_ext = file_url[-4:]

    # file_delimiter = get_delimiter(file_url)
    # file_encoding = get_encoding(file_url)
    result = compare(conf_ext, file_ext)
    if result:
        logging.info("CSV file has an acceptable format")

        df = pd.read_csv(file_url, sep=None, engine="python")

        nested_column = expand_nested(df)

        logging.info("CSV data is extended")

        update_config_schema(schema, nested_column)

        logging.info("Configuration schema is updated")

        if drop_duplicates:
            df.drop_duplicates(inplace=True)

            logging.info("duplicated rows are dropped")

        extended_df = extend_file(df, nested_column)

        formatted_df = compare_schemas(schema, extended_df)
        formatted_df = formatted_df.rename(columns=rename_columns)
        logging.info("Data layers are normalized according to schema")

        return True, formatted_df

    else:

        logging.info("Format is not acceptable")

        return False, {}
