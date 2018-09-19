from time import sleep

from linkedIn_connection.set_up.base_driver import BaseDriver
from linkedIn_connection.utils.json_parser_util import read_config


class MyNetworkPage(object):
    _my_network_tab = "//span[@id='mynetwork-tab-icon']"
    _your_connections_block = "//*[text()='Your connections']"
    _first_candidate_connect_btn = \
        "//h3[text()='People you may know']/../following-sibling::div//li[1]//span[text()='Connect']"
    _config = read_config()

    def move_to_my_network_tab(self):
        BaseDriver().connection.find_element_by_xpath(self._my_network_tab).click()
        assert BaseDriver().connection.find_element_by_xpath(self._your_connections_block).is_displayed()

    def send_connection_request(self):
        for i in range(self._config['TEST']['ITERATIONS_NUM']):
            for j in range(self._config['TEST']['ADD_PER_ITERATION']):
                BaseDriver().connection.find_element_by_xpath(self._first_candidate_connect_btn).click()
                sleep(1)
            BaseDriver().connection.refresh()
            assert BaseDriver().connection.find_element_by_xpath(self._your_connections_block).is_displayed()
