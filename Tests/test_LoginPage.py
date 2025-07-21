import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):


    # def test_signup_link_visible(self):
    #     self.loginPage = LoginPage(self.driver)
    #     flag = self.loginPage.is_signup_link_exist()
    #     assert flag



    def test_signin(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_url(TestData.BASE_URL)
        time.sleep(2)
        title =  self.loginPage.get_login_page_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        print(title,"********************************")
        assert title
