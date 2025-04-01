from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    x_thing = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_thing.text

    ans = str(math.log(abs(12*math.sin(int(x)))))

    form = browser.find_element(By.CSS_SELECTOR, ".form-control")
    form.send_keys(ans)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
