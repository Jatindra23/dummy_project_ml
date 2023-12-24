from project_name.entity.config_entity import DataIngestionConfig,DataValidationConfig , \
DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig

from project_name.utils.utils import read_yaml_file

from project_name.constants import *

from project_name.exception import ProjectException

import sys, os

from project_name.logger import logging

class ConfigurationManager:
    def __init__(self,
         config_file_path:str=CONFIG_FILE_PATH ,   
         currnet_time_stamp:str = CURRENT_TIME_STAMP
         ) ->None:
        try:

            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = currnet_time_stamp

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
           data_ingestion_config = self.config_info[DATA_INGEST_CONFIG_KEY]
           dataset_download_url = data_ingestion_config[DATA_INGEST_DATA_DOWNLOAD_URL_KEY]
           artifact_dir = self.training_pipeline_config.artifact_dir

           data_ingestion_artifact_dir = os.path.join(
               artifact_dir,
               data_ingestion_config[DATA_INGEST_ARTIFACT_DIR],
               self.time_stamp
           )
           
           tgz_download_dir = os.path.join(
               data_ingestion_artifact_dir,
               data_ingestion_config[DATA_INGEST_TGZ_DOWNLOAD_DIR_KEY]
               
           )

           raw_data_dir = os.path.join(
               data_ingestion_artifact_dir,
               data_ingestion_config[DATA_INGEST_RAW_DATA_DIR_KEY]
               
           )

           ingested_data_dir = os.path.join(
               data_ingestion_artifact_dir,
               data_ingestion_config[DATA_INGEST_INGESTED_DIR_KEY]
            
           )

           ingested_train_dir =os.path.join(
               ingested_data_dir,
               data_ingestion_config[DATA_INGEST_INGESTED_TRAIN_DIR_KEY]
           )

           ingested_test_dir = os.path.join(
               ingested_data_dir,
               data_ingestion_config[DATA_INGEST_INGESTED_TEST_DIR_KEY]

           )

           data_ingestion_config = DataIngestionConfig(
               dataset_download_url=dataset_download_url,
               tgz_download_dir=tgz_download_dir,
               raw_data_dir=raw_data_dir,
               ingested_train_dir=ingested_train_dir,
               ingested_test_dir=ingested_test_dir,

                )
           
           logging.info(f"Data Ingestion config: {data_ingestion_config}")

        except Exception as e:
            raise ProjectException(e,sys) from e
        

    def get_data_validation_config(self) ->DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            data_validation_artifact_dir = os.path.join(
                artifact_dir,
                data_validation_config[DATA_VALIDATION_CONFIG_ARTIFACT_DIR],
                self.time_stamp

            )

            data_validataion_schema_file_path = os.path.join(
                data_validation_artifact_dir,
                data_validation_config[DATA_VALIDATION_CONFIG_SCHEME_FILE_NAME]
            )
            

            data_validation_config = DataValidationConfig(

                schema_file_path = data_validataion_schema_file_path

            )

            logging.info("data_validation_config: {data_validation_config}")
        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            data_transformation_config = self.config_info

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_model_trainer_config(self)->ModelTrainerConfig:
        try:
            model_trainer_config = self.config_info

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_trainer_pusher_model(self)->ModelPusherConfig:
        try:
            trainer_pusher_config = self.config_info

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPLINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipline_config = TrainingPipelineConfig(artifact_dir = artifact_dir)
            logging.info(f"Training Pipeline Config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise ProjectException(e,sys) from e
       