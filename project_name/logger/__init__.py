import logging
import os
from datetime import datetime

LOG_DIR = "logs"

current_timer_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

log_file_name = f"log_{current_time_stamp}.log"

os.makedirs(LOG_DIR,exist_ok = True)

log_file_path = os.path.jon(LOG_DIR,log_file_path)

logging.basicConfig(filename = log_file_path,
filemode = "w",
format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level = logging.INFO
)