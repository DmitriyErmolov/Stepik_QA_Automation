from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser  = webdriver.Chrome()
browser.get(link)
# Математическая функция
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, 'book')
    button.click()
    # Решить уже известную нам математическую задачу
    get_x = browser.find_element(By.ID, 'input_value')
    x = calc(get_x.text)
    # Ввести в поле значение X
    input_x = browser.find_element(By.ID, 'answer')
    input_x.send_keys(x)
    # Нажать кнопку Submit
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()
finally:
    time.sleep(3)
    browser.quit()