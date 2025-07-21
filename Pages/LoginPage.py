from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    SEARCH =(By.XPATH,"//input[@id='twotabsearchtextbox']")
    SIGNIN=(By.ID,"nav-link-accountList-nav-line-1")
    #SIGNUP_LINK =
    """Constructor of the page class """
    def __init__(self,driver):
        super().__init__(driver)


    def click_url(self,URL):
        self.driver.get(URL)

    def get_login_page_title(self,title):
        return self.title_is(title)
    def is_signup_link_exist(self,SIGNIN):
        return self.is_visible(SIGNIN)

    # def do_search(self,SIGNIN):
    #     self.do_click(self.SIGNIN)
