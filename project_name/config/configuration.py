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
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_piipeline_config = self.get_training_pipeline_config()

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        try:
           data_ingestion_config = self.config_info

        except Exception as e:
            raise ProjectException(e,sys) from e
    def get_data_validation_config(self) ->DataValidationConfig:
        try:
            data_validation_config = self.config_info

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
       