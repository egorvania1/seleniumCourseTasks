from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    inputAns = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputAns.send_keys(y)

    checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox.click()

    radialBtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radialBtn.click()

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
