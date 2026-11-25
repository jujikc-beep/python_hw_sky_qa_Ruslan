from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru")
    driver.maximize_window()

    driver.add_cookie({
        "name": "SESSION",
        "value": "OTE1NjE1NTYtMGU2Mi00YjBjLTg0ZmUtMmNkNWY2YTk5NTUy",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/jujikc/")

    user1_url = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/xoziaka")

    user2_url = driver.current_url

    result = user1_url != user2_url
    assert result, (
        f"URL не должны совпадать! "
        f"user1_url={user1_url}, user2_url={user2_url}"
    )
    print(result)

    driver.quit()
