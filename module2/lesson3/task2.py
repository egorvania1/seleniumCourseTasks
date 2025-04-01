from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, ".trollface")
    submit.click()

    browser.switch_to.window(browser.window_handles[1])

    x_thing = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_thing.text

    ans = str(math.log(abs(12*math.sin(int(x)))))

    form = browser.find_element(By.CSS_SELECTOR, ".form-control")
    form.send_keys(ans)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
