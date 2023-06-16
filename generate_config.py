import configparser
config_file = configparser.ConfigParser()

config_file.add_section('Reports')
config_file.set('Reports', 'html_report', 'C:\\Users\\aazaizh\\PycharmProjects\\RestApiAutomation\\reports')

with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()