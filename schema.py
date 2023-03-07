import csv
import datetime

# Open the CSV file and read the header row
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

# Define the Snowflake table schema
table_name = 'nyc_data'
column_defs = []
for col_name in header:
    # Determine the data type of the column based on its values
    col_type = 'VARCHAR'
    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row[col_name].isdigit():
                col_type = 'INT'
            elif row[col_name].replace('.', '', 1).isdigit():
                col_type = 'FLOAT'
            elif row[col_name].lower() in ['true', 'false']:
                col_type = 'BOOLEAN'
            elif row[col_name].startswith(('20', '19')) and len(row[col_name]) == 10:
                try:
                    datetime.datetime.strptime(row[col_name], '%Y-%m-%d')
                    col_type = 'DATE'
                except ValueError:
                    pass
    column_defs.append(f"{col_name} {col_type}")
schema_sql = f"CREATE TABLE {table_name} ({', '.join(column_defs)})"

# Print the schema SQL statement
print(schema_sql)
