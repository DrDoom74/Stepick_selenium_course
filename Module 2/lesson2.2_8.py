from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_name("firstname")
    x.send_keys("Ivan")

    x2 = browser.find_element_by_name("lastname")
    x2.send_keys("Petrov")

    x3 = browser.find_element_by_name("email")
    x3.send_keys("test@testmail.com")

    btn = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    btn.send_keys(file_path)

    btn2 = browser.find_element_by_css_selector(".btn")
    btn2.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()