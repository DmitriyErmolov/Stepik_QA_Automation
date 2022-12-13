from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Открыть страницу https://suninjuly.github.io/math.html
link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Считать значение для переменной x
    get_x = browser.find_element(By.ID, 'input_value')
    x = get_x.text
    # Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    new_x = calc(x)
    # Ввести ответ в текстовое поле
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(new_x)
    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()
    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()
    # Нажать на кнопку Submit
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

finally:
    time.sleep(3)
    browser.quit()
