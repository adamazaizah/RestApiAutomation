import configparser
# Method to read config file settings
import os


def read_config():
    config = configparser.ConfigParser()
    try:
        config.read('configurations.ini')
        reports = config["REPORTS"]
        print(reports["html_report"])
    except Exception as e:
        print(os.getcwd())
        return None
    return config

