import pandas as pd
import json


def expand_nested(dataf):
    first_row = dict(dataf.iloc[0])
    last_row = dict(dataf.iloc[-1])
    check_rows = [first_row, last_row]
    for row in check_rows:
        for column, value in row.items():
            try:
                if json.loads(value):
                    return column
            except:
                pass


def compare_schemas(schema_df, extended_df):
    for column in extended_df.columns:
        conf_type = str(schema_df[column].iloc[0])
        file_type = str(extended_df.dtypes[column])
        if file_type in conf_type or conf_type in file_type:
            pass
        else:
            extended_df[column] = "null"
    return extended_df


def extend_file(file_df, nested_col):
    try:
        new = [json.loads(value)
               for value
               in file_df[nested_col].values]

        new_df = pd.DataFrame(new)

        updated_df = file_df.drop(nested_col, axis=1)

        # concatenating two dictionaries into dataframe
        old_dict = updated_df.to_dict()

        new_dict = new_df.to_dict()

        old_dict.update(new_dict)

        res = pd.DataFrame(old_dict)
    except ValueError as e:
        return ValueError(e)

    return res


def compare(conf_ext, file_ext, conf_delimiter,
            file_delimiter, conf_encoding,
            file_encoding):
    result = all([conf_ext == file_ext,
                  conf_delimiter == file_delimiter,
                  conf_encoding == file_encoding]
                 )
    return result
