from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout")))
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Руслан")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Каримов")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("452120")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    driver.quit()

    assert total_text == "Total: $58.29"
