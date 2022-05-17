import csv

import pandas as pd
import chardet


def read_config(config_url):
    conf = pd.read_json(config_url)
    conf = conf["file"]
    ext = conf["ext"]
    delimiter = conf["delimiter"]
    encoding = conf["encoding"]
    columns = list(conf["schema"].keys())
    schema = conf["schema"]
    nested_cols = conf["schema"]["Location"]
    conf_dtypes = conf.dtypes

    # updated_schema = {"Login email": schema["Login email"],
    #                   "Identifier": schema["Identifier"],
    #                   "First name": schema["First name"],
    #                   "Last name": schema["Last name"],
    #                   "city": schema["Location"]["city"],
    #                   "country": schema["Location"]["country"]}

    return ext, delimiter, encoding, columns, schema, \
           nested_cols, conf_dtypes


# TODO : Pass BytesIO object instead of opening file
def get_delimiter(url):
    with open(url, 'r') as csvfile:
        delimiter = csv.Sniffer().sniff(csvfile.readline())
        return delimiter.delimiter


# TODO : Pass BytesIO object instead of opening file
#  (Read documentation of io.BytesIO

def get_encoding(url):
    with open(url, 'rb') as csvfile:
        res = chardet.detect(csvfile.read(10000)) # TODO: Check this
        return res["encoding"]
    # I would have done it differently.
    # p.s you can read only first line and then scan whole file for commas.
    # Amount of commas should be [ number of columns * number of rows ]

def normalization(df):
    # making location values into dictionary'

    new = [eval(value)
           for value
           in df["Location"].values]

    new_df = pd.DataFrame(new)

    # dropping the column "Location" from original df
    # TODO : DO NOT HARDCODE ANY OF THE COLUMNS
    updated_df = df.drop("Location", axis=1)

    # concatenating two dictionaries into dataframe
    old_dict = updated_df.to_dict()

    new_dict = new_df.to_dict()

    old_dict.update(new_dict)

    res = pd.DataFrame(old_dict)

    return res


def compare(conf_ext, file_ext, conf_delimiter,
            file_delimiter, conf_encoding,
            file_encoding, conf_columns,
            file_columns, nested_conf,
            nested_file, conf_dtypes, file_dtypes):
    columns_compare = all(conf_columns == file_columns)
    nested_cols_compare = all([nested_conf == nested_file])

    result = all([conf_ext == file_ext,
                  conf_delimiter == file_delimiter,
                  conf_encoding == file_encoding,
                  columns_compare,
                  nested_cols_compare,
                  conf_dtypes == file_dtypes]
                 )
    return result


# TODO: Write a function to find nested JSON schemas