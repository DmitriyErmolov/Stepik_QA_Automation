from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Открыть страницу http://suninjuly.github.io/get_attribute.html
link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)



# Математическая функция
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    get_number = browser.find_element(By.ID, 'treasure')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = get_number.get_attribute('valuex')
    # Посчитать математическую функцию от x
    math_x = calc(x)
    # Ввести ответ в текстовое поле
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(math_x)
    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    # Нажать на кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

finally:
    time.sleep(3)
    browser.quit()