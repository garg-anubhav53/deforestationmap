import pandas as pd

owdf = pd.read_csv('energy_data_processing/owid-energy-data.csv')
# Display the first few rows of the DataFrame
head = owdf.head()
print(head)
# Display basic information about the DataFrame

datasetinfo = owdf.info()
print(datasetinfo) 
[rows, columns] = owdf.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}") 
# selected_columns = ['Country Name', 'Country Code', '1991', '2021']
selected_columns = ['Country Code', '2021']
# subset_df = df[selected_columns]

column_names = owdf.columns

# Convert column names to a list if needed
column_names_list = column_names.tolist()

# Print the column names
print("Column names:")
for column_name in column_names:
    print(column_name)

column_name = 'country'

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', None)

# Get every row for the specified column
column_data = owdf[column_name]

# Print the column data
print(column_data)


j = ''