from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "FFF"
VERSION = "0.4"
AUTHOR = "Jatindra Paul"
DESCRIPTION = "this is the first machine learning project from the Author"
PACKAGES = find_packages()
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")#removing this  -e because it is used to install the custom packages built by author

#since we are using find_packages from the setuptools so we do not need the  -e .


setup (
name = PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= PACKAGES,
install_requires = get_requirements_list()

)