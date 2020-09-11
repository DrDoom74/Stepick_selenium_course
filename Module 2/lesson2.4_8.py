from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #div.form-group span.nowrap:nth-child(1)
    ##input_value
    # formula = browser.find_element_by_css_selector("div.form-group span.nowrap:nth-child(1)")
    # formula_text = formula.text
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    btn = browser.find_element(By.ID, "book")
    btn.click()

    x = browser.find_element_by_id("input_value")
    x_val = x.text

    y = calc(x_val)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()