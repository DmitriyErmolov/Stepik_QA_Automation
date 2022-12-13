#                   ЗАДАНИЕ:
# 1.Добавьте в самый верх своего кода import math
# 2.Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
# 3.Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
#   str(math.ceil(math.pow(math.pi, math.e)*10000))
# 4.Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
# 5.Заполните скриптом форму так же как вы делали в предыдущем шаге урока
# 6.После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
link = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Добавьте команду, которая найдет ссылку с текстом
    encrypted_num = str(math.ceil(math.pow(math.pi, math.e)*10000))
    # Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
    num = browser.find_element(By.LINK_TEXT, encrypted_num)
    # Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
    num.click()

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
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
# Закрыть браузер через 3 секунды
finally:
    time.sleep(200)
    browser.quit()
