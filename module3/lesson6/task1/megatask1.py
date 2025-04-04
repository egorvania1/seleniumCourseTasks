import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
import math

class TestSite:
    my_email = "NO"
    my_password = "GET OUT OF MY ROOM IM PLAYING MINCERAFT"

    @pytest.mark.skip(reason="Уже вошли")
    def test_login(self, browser):
        browser.implicitly_wait(5)
        browser.get("https://stepik.org/lesson/236895/step/1")

        login_btn = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        login_btn.click()
        email = browser.find_element(By.CSS_SELECTOR, "[name=login]")
        email.send_keys(self.my_email)
        passwd = browser.find_element(By.CSS_SELECTOR, "[name=password]")
        passwd.send_keys(self.my_password)
        login_btn = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
        login_btn.click()
        time.sleep(10)

    @pytest.mark.parametrize('partlink', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_parametr(self, browser, partlink):
        browser.implicitly_wait(10)
        link = f"https://stepik.org/lesson/{partlink}/step/1"
        browser.get(link)

        login_btn = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        login_btn.click()
        email = browser.find_element(By.CSS_SELECTOR, "[name=login]")
        email.send_keys(self.my_email)
        passwd = browser.find_element(By.CSS_SELECTOR, "[name=password]")
        passwd.send_keys(self.my_password)
        login_btn = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
        login_btn.click()
        time.sleep(5)

        inputField = browser.find_element(By.CSS_SELECTOR, '.string-quiz__textarea')
        answer = math.log(int(time.time()))
        inputField.send_keys(answer)
        sendBtn = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        sendBtn.click()
        time.sleep(5)

        hintField = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        text = hintField.text
        assert text == "Correct!", f"Текст не является correct, {text}"
