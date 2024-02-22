import pandas as pd

# Load data from CSV file into a pandas DataFrame

df = pd.read_csv('forest_data_processing/forest_area_km.csv')

# Display the first few rows of the DataFrame
head = df.head()

# Display basic information about the DataFrame

datasetinfo = df.info()

num_rows = len(df)

# selected_columns = ['Country Name', 'Country Code', '1991', '2021']
selected_columns = ['Country Name', '2021']
subset_df = df[selected_columns]

print("\nSummary statistics of the DataFrame:")
print(df.describe())

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Print the full contents of the DataFrame
print(subset_df)
# Display summary statistics of the DataFrame
k = ''
