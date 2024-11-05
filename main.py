from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()

    # Log in
    driver.find_element(by="id", value="id_username").send_keys("automated")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_password")))
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)

    # Wait for the redirection to the dashboard
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

    # Verify the redirection to the dashboard
    current_url = driver.current_url
    if "dashboard" in current_url:
        print(f"Successfully redirected to the dashboard: {current_url}")
    else:
        print(f"Redirection failed. Current URL: {current_url}")

main()
