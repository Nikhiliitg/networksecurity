import os
import sys
import certifi
import json
import ssl
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")# Ensure this is set correctly in your .env file
print(MONGO_DB_URL)

ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Use the correct connection with SSL
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
            tlsCAFile=certifi.where())
            
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            
            # Insert data
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"  # Ensure the file path is correct
    DATABASE = "Nikhiliitg"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    
    # Convert CSV to JSON
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    
    # Insert data into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)