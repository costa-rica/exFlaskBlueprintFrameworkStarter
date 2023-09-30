import os
import json
from dotenv import load_dotenv

load_dotenv()


# with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_file:
#     config_dict = json.load(config_file)
match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            config_dict = json.load(env_file)
        # os.environ["PROJECT_ROOT"] = "/home/nick/applications/exFlaskBlueprintFrameworkStarterWithLogin_dev/"
    case 'prod' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            config_dict = json.load(env_file)
        # os.environ["PROJECT_ROOT"] = "/home/nick/applications/exFlaskBlueprintFrameworkStarterWithLogin/"
    case _:
        print(f"Config_path: {os.environ.get('CONFIG_PATH')}")
        with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            config_dict = json.load(env_file)
        # os.environ["PROJECT_ROOT"] = "/Users/nick/Documents/exFlaskBlueprintFrameworkStarterWithLogin/"

class ConfigBase:

    def __init__(self):

        self.SECRET_KEY = config_dict.get('SECRET_KEY')
        self.PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
        self.DB_ROOT = os.environ.get('DB_ROOT')
        self.DESTINATION_PASSWORD = config_dict.get('DESTINATION_PASSWORD')
        self.DIR_DB_AUXILARY = os.path.join(self.DB_ROOT,"auxilary")


class ConfigLocal(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
            

class ConfigDev(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = True
            

class ConfigProd(ConfigBase):

    def __init__(self):
        super().__init__()

    DEBUG = False


match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev' :
        config = ConfigDev()
        print('- /app_pacakge/config: Development')
    case 'prod' :
        config = ConfigProd()
        print('- /app_pacakge/config: Production')
    case _ :
        config = ConfigLocal()
        print('- /app_pacakge/config: Local')
    
# elif os.environ.get('FLASK_CONFIG_TYPE')=='dev':
#     config = ConfigDev()
#     print('- /app_pacakge/config: Development')
# elif os.environ.get('FLASK_CONFIG_TYPE')=='prod':
#     config = ConfigProd()
#     print('- /app_pacakge/config: Production')
