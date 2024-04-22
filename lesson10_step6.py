from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
browser.get(link)
#browser.implicitly_wait(5)

browser.find_element(By.ID, 'button').click()