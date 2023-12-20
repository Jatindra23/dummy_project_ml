from project_name.entity.config_entity import DataIngestionConfig,DataValidationConfig , \
DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig

from project_name.utils.utils import read_yaml_file

from project_name.constants import *

from project_name.exception import ProjectException

import sys, os

class ConfigurationManager:
    def __init__(self,
         config_file_path:str=CONFIG_FILE_PATH ,   
         currnet_time_stamp:str = CURRENT_TIME_STAMP
         ) ->None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.training_piipeline_config = self.get_training_pipeline_config()

    def gete_data_ingestion_config(self) ->DataIngestionConfig:
        pass

    def get_data_validation_config(self) ->DataValidationConfig:
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_trainer_pusher_model(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            aritfact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPLINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )



        except Exception as e:
            raise ProjectException(e,sys) from e
       