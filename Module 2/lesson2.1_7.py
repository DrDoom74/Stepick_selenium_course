from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    val1 = int(num1.txt)
    val2 = int(num2.txt)
    val = val1 + val2

    select = Select(browser.find_element_by_tag_name("select"))
    variant = select.select_by_value(str(val))

    variant.click()

    submit = browser.find_element_by_css_selector(".btn.btn-default")
    submit.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()