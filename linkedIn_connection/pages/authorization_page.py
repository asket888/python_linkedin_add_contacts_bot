from linkedIn_connection.set_up.base_driver import BaseDriver
from linkedIn_connection.utils.json_parser_util import read_config


class AuthorizationPage(object):
    _url = "https://www.linkedin.com"
    _login_inp = "//input[@id='login-email']"
    _password_inp = "//input[@id='login-password']"
    _submit_btn = "//input[@id='login-submit']"
    _config = read_config()

    def login_to_application(self):
        BaseDriver().connection.get(self._url)
        BaseDriver().connection.find_element_by_xpath(self._login_inp).send_keys(self._config['E_MAIL'])
        BaseDriver().connection.find_element_by_xpath(self._password_inp).send_keys(self._config['PASSWORD'])
        BaseDriver().connection.find_element_by_xpath(self._submit_btn).click()
        assert BaseDriver().connection.find_element_by_xpath("//*[text()='"+self._config['USER_NAME']+"']").is_displayed()
