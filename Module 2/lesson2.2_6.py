from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #div.form-group span.nowrap:nth-child(1)
    ##input_value
    # formula = browser.find_element_by_css_selector("div.form-group span.nowrap:nth-child(1)")
    # formula_text = formula.text

    x = browser.find_element_by_id("input_value")
    x_val = x.text

    y = calc(x_val)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()