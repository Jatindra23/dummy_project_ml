import os
from datetime import datetime

ROOT_DIR = os.getcwd() #To get current working directory


CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_DIR = "config"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FILE_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#training_pipeline_config
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPLINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "aritfcat"


#Data _Ingestion_Config Constant Variables:

DATA_INGEST_CONFIG_KEY = "data_ingestion_config"
DATA_INGEST_ARTIFACT_DIR = "data_ingestion"
DATA_INGEST_DATA_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGEST_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGEST_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGEST_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGEST_INGESTED_TRAIN_DIR_KEY = "ingestd_train_dir"
DATA_INGEST_INGESTED_TEST_DIR_KEY = "ingested_test_dir"


#Data_validation_config Variables:

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_CONFIG_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_CONFIG_SCHEME_FILE_NAME = "schema.yaml"


#Data_transformation_config Variables

DATA_TRANSFORM_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORM_CONFIG_KEY = "data_transformation"
DATA_TRANSFORM_DIR_KEY = "transformed_data"
DATA_TRANSFORM_TRAIN_DIR_KEY = "train"
DATA_TRANSFORM_TEST_DIR_KEY = "test"
DATA_TRANSFORM_PREPROSSESING_DIR_KEY = "preprocessed"
DATA_TRANSFORM_PREPROCESSED_OBJECT_FILE_NAME_PATH = "processed.pkl"


#model_trainer_config Variables

MODEL_TRAINER_CONFIG_KEY  = "model_trainer_config"
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MODEL_TRAINER_MODEL_FILE_NAME_PATH ="model.pkl"
MODEL_TRAINER_BASE_ACCURACY = 0.6 


#model_evaluation_config Variables

MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"
MODEL_EVALUATION_CONFIG_KEY= "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_PATH = "model_evaluation.yaml"


#trainer_pusher_config Variable

MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_ARTIFACT_DIR = "modle_pusher"
MODEL_PUSHER_EXPORT_DIR_KEY = "saved_models"