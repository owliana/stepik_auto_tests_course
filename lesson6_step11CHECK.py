from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_input = browser.find_element(By.CLASS_NAME, "first")
    first_input.send_keys("Ivan")
    second_input = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
    second_input.send_keys("Ivanov")
    third_input = browser.find_element(By.CLASS_NAME, "third")
    third_input.send_keys("Ivanov@mail.ru")
    # Отправляем заполненную форму
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()