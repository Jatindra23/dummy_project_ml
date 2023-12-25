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
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_config = self.config_info[DATA_TRANSFORM_CONFIG_KEY]

            data_transformation_artifact_dir = os.path.join(
                artifact_dir,
                data_transformation_config[DATA_TRANSFORM_ARTIFACT_DIR],
                self.time_stamp
            )

            transformed_dir = os.path.join(

                data_transformation_artifact_dir,
                data_transformation_config[DATA_TRANSFORM_DIR_KEY]

            )

            transformed_train_dir = os.path.join(

                transformed_dir,
                data_transformation_config[DATA_TRANSFORM_TRAIN_DIR_KEY]

            )

            transformed_test_dir = os.path.join(
                transformed_dir,
                data_transformation_config[DATA_TRANSFORM_TEST_DIR_KEY]

            )

            preprocessing_dir  = os.path.join(

                data_transformation_artifact_dir,
                data_transformation_config[DATA_TRANSFORM_PREPROSSESING_DIR_KEY]

            )

            preprocessed_object_file_path = os.path.join(

                preprocessing_dir,
                data_transformation_config[DATA_TRANSFORM_PREPROCESSED_OBJECT_FILE_NAME_PATH]

            )

            data_transformation_config = DataTransformationConfig(

                transformed_test_dir=transformed_test_dir,
                transformed_train_dir=transformed_train_dir,
                preprocessed_object_file_path=preprocessed_object_file_path

            )

            logging.info(f"DataTransformationConfig: {data_transformation_config}")

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_config = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            artifact_dir = self.training_pipeline_config.artifact_dir

            model_trainer_artifact_dir = os.path.join(

                artifact_dir,
                model_trainer_config[MODEL_TRAINER_ARTIFACT_DIR],
                self.time_stamp 

            )

            trained_model_dir = os.path.join(

                model_trainer_artifact_dir,
                model_trainer_config[MODEL_TRAINER_TRAINED_MODEL_DIR]

            )

            trained_model_file_path = os.path.join(

                trained_model_dir,
                model_trainer_config[MODEL_TRAINER_MODEL_FILE_NAME_PATH]

            )

            base_accuracy =model_trainer_config[MODEL_TRAINER_BASE_ACCURACY]

            model_trainer_config = ModelTrainerConfig(

                trained_model_file_path=trained_model_file_path,
                base_accuracy=base_accuracy

            )

            logging.info(f"model_trainer_config: {model_trainer_config}")
                         
        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            artifact_dir = self.training_pipeline_config.artifact_dir

            model_evaluation_artifact_dir = os.path.join(

                artifact_dir,
                model_evaluation_config[MODEL_EVALUATION_ARTIFACT_DIR],
                self.time_stamp

            )

            model_evaluation_file_name_path = os.path.join(
                model_evaluation_artifact_dir,
                model_evaluation_file_name_path
            )




            model_evaluation_config = ModelEvaluationConfig(
                model_evaluation_file_path=model_evaluation_file_name_path,
                time_stamp=self.time_stamp
            )

            logging.info(f"model_evaluation_config: {model_evaluation_config}")

        except Exception as e:
            raise ProjectException(e,sys) from e

    def get_model_pusher_model(self)->ModelPusherConfig:
        try:
            model_pusher_config = self.config_info[MODEL_PUSHER_CONFIG_KEY]

            artifact_dir = self.training_pipeline_config.artifact_dir

            model_pusher_artifact_dir = os.path.join(

                artifact_dir,
                model_pusher_config[MODEL_PUSHER_ARTIFACT_DIR],
                self.time_stamp

            )


            model_pusher_export_dir_path = os.path.join(

                model_pusher_artifact_dir,
                model_pusher_config[MODEL_PUSHER_EXPORT_DIR_KEY]
                
            )

            model_pusher_config = ModelPusherConfig(

                export_dir_path=model_pusher_export_dir_path

            )

            logging.info(f"model_pusher_config: {model_pusher_config}")

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
       