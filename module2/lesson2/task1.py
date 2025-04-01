from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x, y):
  return str(x + y)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)

    res = calc(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(res)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

