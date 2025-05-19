import configparser
import os
config = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "Configurations", "config.ini")
config.read(config_file_path)

class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('basic info', 'url')
        return url

    @staticmethod
    def get_email():
        email = config.get('basic info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('basic info', 'password')
        return password

