import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    add = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    add_text = add.text
    assert add_text, 'Кнопка не найдена'
    print(add_text)