import unittest

from linkedIn_connection.set_up.base_driver import BaseDriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = BaseDriver().remote_driver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
