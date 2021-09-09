import configparser 

class Base(object):

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        self.cloud_name: str = config["credential"]["HOSTNAME"]
        self.base_url: str = f"https://admin.{self.cloud_name}/api/v1"
        self.api_key: str = config["credential"]["APIKEY"]
        self.admin_user: str = config["credential"]["USERNAME"]
        self.admin_password: str = config["credential"]["PASSWORD"]
