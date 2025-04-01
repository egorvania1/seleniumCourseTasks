from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputName = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    inputName.send_keys("Mario")
    inputSurname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    inputSurname.send_keys("Mario")
    inputEmail = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    inputEmail.send_keys("mariomario@itsame.com")

    fileSender = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'cv.txt')
    fileSender.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
