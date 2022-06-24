from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)

    browser.get(link)

    button1 = browser.find_element(By.ID, "button")
    button1.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()