from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()

#browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")