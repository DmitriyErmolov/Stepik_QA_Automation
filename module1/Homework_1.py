from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Открыть ссылку в браузере
link = 'http://suninjuly.github.io/simple_form_find_task.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ввести в поле "First name" значение "Dmitry"
    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Dmitry')
    # Ввести в поле "Last name" значение "Ermolov"
    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Ermolov')
    # Ввести в поле "City" значение "Moscow"
    city = browser.find_element(By.NAME, 'firstname')
    city.send_keys('Moscow')
    # Ввести в поле "Country" Значение "Russia"
    country = browser.find_element(By.ID, 'country')
    country.send_keys('Russia')
    # Кликнуть кнопку "Submit" Для отправки формы
    submit_button = browser.find_element(By.ID, 'submit_button')
    submit_button.click()
# Закрыть браузер через 3 секунды
finally:
    time.sleep(3)
    browser.quit()

