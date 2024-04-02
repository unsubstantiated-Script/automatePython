from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://youtu.be/YlcY_enzwmI?si=zc4nQrhhMCk6hty0&t=31')

WebDriverWait(browser, 8).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-label='Play']"))).click()
