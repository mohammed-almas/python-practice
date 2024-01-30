import csv
import pandas as pd
import io

FILE_NAME = 'forParsing_task.xls'

# with open(FILE_NAME, 'r') as file:
#     fileContent = csv.DictReader(file)
#     for content in fileContent:
#         print(content)


# file_content = pd.read_csv('output.csv')
# file_content = pd.read_excel(FILE_NAME, engine='xlrd')
# print(file_content)

# file_content.to_csv('test.csv', index=None, header=True)
# df = pd.DataFrame(pd.read_csv('test.csv'))

# print(df)


def format_rows(file_data):
    data_list = [row.replace('\n', '').strip() for row in file_data]

    final_list = []

    for row in data_list:
        if (
            row.startswith('Customer') or
            row.startswith('Code') or
            row.startswith('Name') or
            row.startswith('City') or
            row=='' or
            row.startswith('|--') or
            row.startswith('--')
        ):
            pass
        else:
            data = [r.strip() for r in row[1:-2].split('|')]
            if (len(final_list) != 0 and data == final_list[0]):
                continue

            final_list.append(data)
    
    return final_list


def convert_xl_to_csv(file_name):
    with io.open(file_name, "r", encoding="utf-8") as file:
        data = file.readlines()

    formatted_rows = format_rows(data)
    column_names = formatted_rows[0]
    print(formatted_rows)

    df = pd.DataFrame(formatted_rows[1:], columns=column_names)
    print(df)

    df.to_csv('temp.csv', header=True, index=False, sep=';')


if __name__ == "__main__":
    convert_xl_to_csv(FILE_NAME)
