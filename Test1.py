import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.mumzworld.com/en")
driver.maximize_window()
time.sleep(3)

SearchBox = driver.find_element(By.ID, "search_textbox")
SearchBox.send_keys("Clevamama - Toddler Pillow - White/Blue")
SearchBox.send_keys(Keys.RETURN)
time.sleep(5)

CartItem = driver.find_element(By.ID, "add_cart_button")
CartItem.click()
time.sleep(5)

Cart = driver.find_element(By.ID, "cart_button")
Cart.click()
time.sleep(5)

for _ in range(4):
    IncreaseQty = driver.find_element(By.ID, "increase_button")
    IncreaseQty.click()
    time.sleep(3)

Checkout = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/div[2]/section/div[3]/button")
Checkout.click()
time.sleep(5)

CreateAccountPage = driver.find_element(By.ID, "create_account_button")
CreateAccountPage.click()
time.sleep(5)

FirstName = driver.find_element(By.ID, "firstname")
FirstName.send_keys("Thisara")
time.sleep(3)
LastName = driver.find_element(By.ID, "lastname")
LastName.send_keys("Thalagala")
time.sleep(3)
Email = driver.find_element(By.ID, "email")
Email.send_keys("Thisara@gmail.com")
time.sleep(3)
Password = driver.find_element(By.ID, "password")
Password.send_keys("Thisara@111")
time.sleep(3)
CreateAccount = driver.find_element(By.ID, "register_btn")
CreateAccount.click()
time.sleep(20)

driver.close()
driver.quit()

print("Test Complete")
print("Test Complete")
