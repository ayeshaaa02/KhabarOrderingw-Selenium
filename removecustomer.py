from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'C:\Users\USER\Videos\selenium test app\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get('file:///C:/Users/USER/Videos/selenium%20test%20app/index.html')
    time.sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, '[data-selenium-id="username-input"]').send_keys('admin')
    driver.find_element(By.CSS_SELECTOR, '[data-selenium-id="password-input"]').send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, '[data-selenium-id="login-button"]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-selenium-id="remove-user-button"]').click()
    time.sleep(2)
    print("customer removed!")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(2)
    driver.quit()