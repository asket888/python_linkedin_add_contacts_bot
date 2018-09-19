import unittest

from linkedIn_connection.set_up.base_test import BaseTest
from linkedIn_connection.pages.my_network_page import MyNetworkPage
from linkedIn_connection.pages.authorization_page import AuthorizationPage


class LinkedInSendConnectionRequestTest(BaseTest):

    def test_linkedIn_add_connection(self, authorization_page=AuthorizationPage(), my_network_page=MyNetworkPage()):
        authorization_page.login_to_application()
        my_network_page.move_to_my_network_tab()
        my_network_page.send_connection_request()


if __name__ == "__main__":
    unittest.main()
