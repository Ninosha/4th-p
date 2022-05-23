import pandas as pd

config_url = r"C:\Users\pc\PycharmProjects\4th-p\conf.json"

url = r"C:\Users\pc\Downloads\email.csv"

df = pd.read_csv(url)


def get_schema(file, nested_column):
    """This function loads the given schema available"""
    df1 = pd.read_json(file)
    schema = pd.json_normalize(df1["file"]["schema"])
    schema.columns = schema.columns.str.replace(f'{nested_column}.', '')
    return schema


conf_schema = get_schema(config_url, "Location")


def expand_nested(dataf):
    first_row = dict(dataf.iloc[0])
    for column, value in first_row.items():
        try:
            if eval(value):
                return column
        except:
            pass


def compare_schemas(schema_df, extended_df):
    schema_status = True
    for column in extended_df.columns:
        conf_type = str(schema_df[column].iloc[0])
        file_type = str(extended_df.dtypes[column])
        if file_type in conf_type or conf_type in file_type:
            pass
        else:
            schema_status = False
    return schema_status
#