import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    cartButton = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert cartButton, "Не найдена кнопка добавления в корзину"
    #time.sleep(30)

