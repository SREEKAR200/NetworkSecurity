from NetworkSecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from NetworkSecurity.entity.config_entity import DataValidationConfig
from NetworkSecurity.exceptions.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from NetworkSecurity.utils.main_utils.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
from NetworkSecurity.utils.main_utils.utils import read_yaml_file
import os,sys


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception  as e:
            raise NetworkSecurityException(e,sys)
    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def validate_number_of_columns(self,dataframe:pd.DataFrame)-> bool:
        try:
            number_of_Columns=len(self.._schema_config)
            logging.info(f"Required Number of Columns:{number_of_Columns}")
            logging.info(f"DataFrame has Columns:{len(dataframe.columns)}")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df{column}
                d2=current_df[column]
                is_same_dist=ks_2samp(d1,d2)
                if threshold<=is_same_dist.pvalue:
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(is_same_dist.pvalue),
                    "drift_Status":is_found

                }})
            drift_report_file_path=self.data_validation_config.drift_report_file_path
            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)

        except  Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"{error_message} Train dataframe does not contain all columns"
            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f"{error_message} Test dataframe does not contain all columns"
        except Exception as e:
            raise NetworkSecurityException

