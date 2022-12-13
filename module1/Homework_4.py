# Вам дана страница с формой регистрации. Проверьте, что можно зарегистрироваться на сайте,
# заполнив только обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей может быть любым.
# Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице,
# которая открывается после регистрации.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Открыть страницу "http://suninjuly.github.io/registration1.html"
link = 'http://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ввести в поле "First name" значение "Dmitry"
    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    first_name.send_keys('Dmitry')
    # Ввести в поле "Last name" значение "Ermolov"
    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    last_name.send_keys('Ermolov')
    # Ввести в поле "Email name" значение "test@yandex.ru"
    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email.send_keys('test@yandex.ru')
    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
    # Сравнить сообщение об успешной регистрации с ожидаемым результатом
    msg = browser.find_element(By.TAG_NAME, 'h1')
    msg_text = msg.text
    assert msg_text == 'Congratulations! You have successfully registered!', 'Ожидаемое сообщение не соответствует фактическому'

finally:
    # Закрыть браузер через 3 секунды
    time.sleep(3)
    browser.quit()