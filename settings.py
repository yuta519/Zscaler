import os
from os.path import join, dirname
from dotenv import load_dotenv

def getId():
        load_dotenv(verbose=True)
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        API = os.environ.get("API_KEY")
        USR = os.environ.get("USER_NAME")
        PWD = os.environ.get("PASSWORD")
        HST = os.environ.get("HOST_NAME")
        id_value = [API, USR, PWD, HST]
        return id_value