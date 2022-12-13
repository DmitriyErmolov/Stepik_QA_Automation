from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



# Открыть страницу http://suninjuly.github.io/file_input.html
link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    first_name.send_keys('Dmitry')

    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    last_name.send_keys('Ermolov')

    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    email.send_keys('Test@yandex.ru')
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')
    download_file = browser.find_element(By.ID, 'file')
    download_file.send_keys(file_path)
    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
finally:
    time.sleep(3)
    browser.quit()

