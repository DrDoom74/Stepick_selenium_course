from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #div.form-group span.nowrap:nth-child(1)
    ##input_value
    # formula = browser.find_element_by_css_selector("div.form-group span.nowrap:nth-child(1)")
    # formula_text = formula.text

    btn = browser.find_element_by_css_selector(".trollface.btn")
    btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x = browser.find_element_by_id("input_value")
    x_val = x.text

    y = calc(x_val)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()