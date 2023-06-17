import configparser
# Method to read config file settings
import os

from Consts import ProjectConsts


def read_config():
    config = configparser.ConfigParser()
    ROOT_DIR = ProjectConsts.ROOT_DIR
    try:
        config.read(f'{ROOT_DIR}//configurations.ini')
        reports = config["REPORTS"]
        print(reports["html_report"])
    except Exception as e:
        print(os.getcwd())
        return None
    return config

