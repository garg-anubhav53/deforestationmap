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
# subset_df = df[selected_columns]

column_names = owdf.columns

# Convert column names to a list if needed
column_names_list = column_names.tolist()

# Print the column names
print("Column names:")
for column_name in column_names:
    print(column_name)

column_names = ['iso_code', 'year', 'coal_consumption', 'gas_consumption']
pd.set_option('display.min_rows', 300)
pd.set_option('display.max_rows', 300)

pd.set_option('display.max_columns', None)

# Filter out rows with blank data for the selected column
filtered_data = owdf.dropna(subset=column_names)

# Print the filtered column data
print(filtered_data[column_names])

# Print the filtered data
print(filtered_data)

# Specify multiple ISO codes
select_iso_codes = ['VNM', 'UZB', 'BLR', 'DEU']

# Filter rows where a specific column matches any of the ISO codes
filtered_data = owdf.loc[owdf['iso_code'].isin(select_iso_codes)].dropna(subset=column_names)

# Print the filtered data
print(filtered_data[column_names])

j = ''