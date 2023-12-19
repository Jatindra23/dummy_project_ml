import os
from datetime import datetime

ROOT_DIR = os.getcwd() #To get current working directory


CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_DIR = "config"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FILE_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"