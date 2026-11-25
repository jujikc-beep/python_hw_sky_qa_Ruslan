from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_btn.click()

    hello_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )

    driver.save_screenshot("screenshots/hello_world.png")

    assert hello_element.is_displayed()
    driver.quit()
    