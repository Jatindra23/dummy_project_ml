import yaml
from project_name.exception import ProjectException
import os 
import sys

def read_yaml_file(file_path:str)-> dict:

    """
    Reads the .yaml file and returns as a dictionary type 
    with using a parameter file_path 
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise ProjectException(e,sys) from e