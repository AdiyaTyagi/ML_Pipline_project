import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")

#notebook\data\income_cleandata.csv

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            logging.info("Data reading using Pandas library from local system")
            data = pd.read_csv(os.path.join("notebook/data", "income_cleandata.csv"))
            logging.info("Data reading completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Data splited into train and test")

            train_set, test_set = train_test_split(data, test_size = .30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
        except Exception as e:
            logging.info("Error occured in Data Ingestion stage")
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()