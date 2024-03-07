import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get("common data", "base_url")
        return url

    @staticmethod
    def get_username():
        user = config.get("common data", "user_email")
        return user

    @staticmethod
    def get_password():
        pwd = config.get("common data", "password")
        return pwd

