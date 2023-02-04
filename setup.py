from setuptools import setup
from typing import List


PROJECT_NAME="housing-prediction"
VERSION="0.0.1"
AUTHOR="payal talmale"
DESCRIPTION="this is the first   machine learning project"
PACKEGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,  
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packeges=PACKEGES,
install_requires=get_requirements_list()
)


