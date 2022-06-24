from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # скроллим до button
    #    button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #radiobutton
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    #checkbox
    option2 = browser.find_element_by_id("robotCheckbox")
    option2.click()

    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()