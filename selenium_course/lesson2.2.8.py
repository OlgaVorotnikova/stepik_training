from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем форму
    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Olga")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("V")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("O@m.ru")

    # загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file2.2.8.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()