from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)

    res = calc(x)

    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(res)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox.click()

    radialBtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radialBtn.click()


    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

