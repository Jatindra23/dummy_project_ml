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


#Data _Ingestion_config
DATA_INGEST_CONFIG_KEY = "data_ingestion_config"
DATA_INGEST_DATA_DOWNLOAD_URL = "dataset_download_url"
DATA_INGEST_RAW_DATA_DIR = "raw_data_dir"
DATA_INGEST_TGZ_DOWNLOAD_DIR = "tgz_download_dir"
DATA_INGEST_INGESTED_DIR = "ingested_dir"
DATA_INGEST_INGESTED_TRAIN_DIR = "ingestd_train_dir"
DATA_INGEST_INGESTED_TEST_DIR = "ingested_test_dir"


#