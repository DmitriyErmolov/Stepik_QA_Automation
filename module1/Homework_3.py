# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку.
# Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
# Теперь эта задача под силу только роботам.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Откроем страницу: http://suninjuly.github.io/find_link_text
link = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Перебираем циклом все и записываем в каждое поле "test answer"
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for element in elements:
        element.send_keys('test answer')
    # Нажимаем кнопку "Submit" для отправки формы
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
# Закрываем браузер через 3 секунды
finally:
    time.sleep(3)
    browser.quit()