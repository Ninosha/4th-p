# import csv
# import pandas as pd
# import chardet
#
#
# # def check_types(df, value_type, value, conf_type,  file_type):
# #     print(file_type)
# #     if "object" in file_type and "str" in conf_type:
# #         if "str" in value_type and value.isnumeric():
# #             print(value)
# #             df = \
# #                 df.replace(to_replace=value, value="gh")
# #             print(df)
# #             return df
# #         # if "int" in value_type and value.astype(int):
# #         #     df = \
# #         #         df.replace(to_replace=value, value="null")
# #         #     return df
#
#
# def expand_nested(dataf):
#     first_row = dict(dataf.iloc[0])
#     last_row = dict(dataf.iloc[-1])
#     check_rows = [first_row, last_row]
#     for row in check_rows:
#         for column, value in row.items():
#             try:
#                 if eval(value):
#                     return column
#             except Exception as e:
#                 pass
#
#
# # def check_int(df, value, column, type):
# #     if isinstance(type, str):
# #         try:
# #             int(value)
# #             print(value)
# #             df = df[column].replace([value], "null")
# #
# #         except:
# #             pass
# # if type == "int" and isinstance(type(value), str):
# #     df[column].replace([value], "null")
# def h(extended_df, value_type, conf_type, column, value):
#     if value_type in conf_type or conf_type in value_type:
#         # print("all good")
#         pass
#
#     else:
#         # print("changing to null")
#         extended_df[column] = \
#             extended_df[column].replace([value], "null")
#
#
# def compare_schemas(schema_df, extended_df):
#     schema_status = True
#     wrong_types = []
#     for column in extended_df.columns:
#         conf_type = str(schema_df[column].iloc[0])
#         file_type = str(extended_df.dtypes[column])
#         for value in extended_df[column].values:
#             value_type = str(type(value))
#             if "object" in file_type and "str" in conf_type:
#                 if "str" in value_type and value.isnumeric():
#                     extended_df = \
#                         extended_df.replace(to_replace=value,
#                                             value="null")
#                     h(extended_df, value_type, conf_type, column, value)
#
#     print(extended_df)
#
#     # new_df = extended_df.apply(lambda x: None)
#     # test = lambda x: True if (x > 10 and x < 20) else extended_df[column].replace([], null)
#     #
#     # if file_type in conf_type or conf_type in file_type:
#     #     pass
#     # else:
#     #     schema_status = False
#     #     wrong_types.append(column)
#
#     return extended_df
#
#
# def read_config(config_url, nested_column):
#     conf_df = pd.read_json(config_url)
#     conf_df = conf_df["file"]
#     ext = conf_df["ext"]
#     delimiter = conf_df["delimiter"]
#     encoding = conf_df["encoding"]
#     schema = pd.json_normalize(conf_df["schema"])
#     drop_duplicates = conf_df["drop_duplicates"]
#     schema.columns = schema.columns.str.replace(f'{nested_column}.', '')
#
#     return ext, delimiter, encoding, schema, drop_duplicates
#
#
# def get_delimiter(url):
#     with open(url, 'r') as csvfile:
#         delimiter = csv.Sniffer().sniff(csvfile.readline()).delimiter
#         return delimiter
#
#
# def get_encoding(url):
#     with open(url, 'rb') as csvfile:
#         res = chardet.detect(csvfile.read())
#         return res["encoding"]
#
#
# #
# def normalization(file_df, nested_col):
#     # making location values into dictionary'
#     # new = [eval(value) if
#     #        isinstance(type(eval(value)), dict)
#     #        else
#     #        file_df[nested_col].replace([value], "null")
#     #        for value
#     #        in file_df[nested_col].values
#     #        ]
#
#     new = [eval(value)
#            for value
#            in file_df[nested_col].values]
#
#     new_df = pd.DataFrame(new)
#
#     updated_df = file_df.drop(nested_col, axis=1)
#
#     # concatenating two dictionaries into dataframe
#     old_dict = updated_df.to_dict()
#
#     new_dict = new_df.to_dict()
#
#     old_dict.update(new_dict)
#
#     res = pd.DataFrame(old_dict)
#
#     return res
#
#
# def compare(conf_ext, file_ext, conf_delimiter,
#             file_delimiter, conf_encoding,
#             file_encoding):
#     result = all([conf_ext == file_ext,
#                   conf_delimiter == file_delimiter,
#                   conf_encoding == file_encoding]
#                  )
#     return result

import json
test_string = '{"city" : "Tbilisi", "country":"Georgia"}'
res = json.loads(test_string)
print(res)