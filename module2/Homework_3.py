from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открыть страницу https://suninjuly.github.io/selects1.html
link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # Посчитать сумму заданных чисел
    get_num_1 = browser.find_element(By.ID, 'num1')
    num_1 = get_num_1.text

    get_num_2 = browser.find_element(By.ID, 'num2')
    num_2 = get_num_2.text

    sum_of_nums = int(num_1) + int(num_2)
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum_of_nums))
    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

finally:
    time.sleep(3)
    browser.quit()
