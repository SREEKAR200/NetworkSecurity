import os
import numpy as np 
import sys
import pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="phishingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

DATA_INGESTION_COLLECTION_NAME:str="Network_data"
DATA_INGESTION_DATABASE_NAME:str="NetworksAI"
DATA_INGESTION_DIR_NAME:str="DataIngestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="Ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2
