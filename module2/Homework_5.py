from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



# Открыть страницу http://suninjuly.github.io/alert_accept.html
link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
# Математическая функция
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    # Нажать на кнопку
    button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]')
    button.click()
    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    get_num = browser.find_element(By.ID, 'input_value')
    num = get_num.text
    change_num = calc(num)
    # Ввести число с ответом в поле
    input_num = browser.find_element(By.ID, 'answer')
    input_num.send_keys(change_num)
    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
finally:
    time.sleep(3)
    browser.quit()

