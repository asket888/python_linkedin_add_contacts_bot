from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from linkedIn_connection.utils.json_parser_util import read_config


class BaseDriver(object):
    __driver = None
    _config = read_config()
    _CHROME_DRIVER_PATH = "C:\\Users\\asket\\PycharmProjects\\selenium_test\\browsers\\chromedriver.exe"

    def __new__(cls, *args, **kwargs):
        if not cls.__driver:
            cls.__driver = super(BaseDriver, cls).__new__(cls, *args, **kwargs)
        return cls.__driver

    def remote_driver(self, *args, **kwargs):
        if self._config['BROWSER'] == "CH_GUI":
            self.connection = webdriver.Chrome(executable_path=self._CHROME_DRIVER_PATH)
        elif self._config['BROWSER'] == "CH_HEADLESS":
            options = Options()
            options.headless = True
            options.add_argument('window-size=1200x800')
            self.connection = webdriver.Chrome(chrome_options=options, executable_path=self._CHROME_DRIVER_PATH)
        else:
            raise AttributeError("Wrong Browser. Check your config file please")
        return self.connection
