import configparser

config = configparser.RawConfigParser()

config.read('.//configurations/config.ini')


class ReadConfig():
    def LoginUrl(self):
        url = config.get('Login details','baseURL')
        return url
    def LoginID(self):
        id=config.get('Login details','username')
        return id
    def LoginPwd(self):
        pwd = config.get('Login details','password')
        return pwd