from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData


@pytest.fixture(scope="class")
def init_driver(request):

    #if request.param =="Chrome":
    web_driver=webdriver.Chrome()



    # if request.param =="firefox":
    #     web_driver =webdriver.Chrome(executable_path=TestData.EDGE_EXECUTABLE_PATH)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(4)
    yield
    web_driver.close()
