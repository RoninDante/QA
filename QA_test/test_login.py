from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Тест 1: Успешный логин
def test_valid_login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    print("✅ Тест 1 пройден: успешный логин")

# Тест 2: Ошибка при неверном пароле
def test_invalid_login():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in error.text
    print("✅ Тест 2 пройден: ошибка при неверном пароле")

# Тест 3: Добавление товара в корзину
def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
    print("✅ Тест 3 пройден: товар добавлен в корзину")

# Запуск тестов
test_valid_login()
test_invalid_login()
test_add_to_cart()

driver.quit()
