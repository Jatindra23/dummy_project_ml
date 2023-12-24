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

