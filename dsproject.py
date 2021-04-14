#!/usr/bin/env python3
import json
import csv
import os
import pandas as pd 


# 1. Fetch / download / retrieve a remote data file by URL, S3 key, or
# ingest a local file mounted to the container.
remotefile = os.getenv('REMOTEURL')
data = pd.read_csv(remotefile)

# To test my ETL data processor, I used a CSV from Github of Covid-19 cases reported on college and university campuses
# in the United States from The New York Times.
    # covid19 = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/colleges/colleges.csv')


# 2. Convert the general format and data structure of the data source
# (from TSV to CSV, from CSV to JSON, from JSON into a SQL database table, etc.)  
def convert_to_json(data):
   data.to_json(r'output.json')

# I converted the covid19 data to a json file that saved to my directory.
    # convert_to_json(covid19)


# 3. Modify the number of columns from the source to the destination, reducing or adding columns.
def remove_col(data, colname):
    data.drop([colname], axis='columns', inplace=True)
    
# Because I found these columns to be unnecessary, I removed the notes and ipeds_id columns from the covid19 data.
    # remove_col(covid19,'notes')
    # remove_col(covid19, 'ipeds_id')


# 5. Generate a brief summary of the data file ingestion including:
#        a. Number of records
#        b. Number of columns

def summary(data):
    print('This data file ingestion has ' + str(len(data.columns)) + ' columns.')
    print('This data file ingestion has ' + str(len(data.index)) + ' records.')

# I printed a summary of the covid19 data that stated:
    # This data file ingestion has 7 columns.
    # This data file ingestion has 1949 records. 
# summary(covid19)
    
