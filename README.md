# DS3002Project
ETL Data Processor

In this project, I authored a segment of an ETL pipeline that will ingest or process raw data. The data processr is able to ingest a pre-defined data source and perform these operations:
  1. Fetch / download / retrieve a remote data file by URL.
  2. Convert the general format and data structure of the data source (from CSV to JSON).
  3. Modify the number of columns from the source to the destination, reducing columns.
  4. Generate a brief summary of the data file ingestion including:
      - Number of records
      - Number of columns
        
List of Functions:
1. def convert_to_json(data):  
  data.to_json(r'output.json')
    - This function converts the ingested data to json format by using a built-in function in pandas (to_json).
2. def remove_col(data, colname):  
data.drop([colname], axis='columns', inplace=True)
    - This function drops columns given data and a column name that is to be dropped.
3. def summary(data):  
print('This data file ingestion has ' + str(len(data.columns)) + ' columns.')  
print('This data file ingestion has ' + str(len(data.index)) + ' records.')
    - This function generates a brief summary of the data file ingestion including the number of records and columns.
