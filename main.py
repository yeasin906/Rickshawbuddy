from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
driver_path = "C:\\Program Files\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

def test_navigate_to_homepage():
    try:
        driver.get("http://127.0.0.1:8000/")
        print("Test Case 1: Navigated to homepage successfully")
        time.sleep(3)  
    except Exception as e:
        print(f"Test Case 1: Failed due to {str(e)}")

def signup_test():
    try:
        driver.get("http://127.0.0.1:8000/")

        # Fill in the Username field
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='User Name']"))
        )
        username_input.clear()
        username_input.send_keys("Khadiza")

        # Fill in the Email field
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']"))
        )
        email_input.clear()
        email_input.send_keys("khadiza@example.com")

        # Fill in the Password field
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_input.clear()
        password_input.send_keys("12345")

        # Click the Signup button
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/form/input[5]"))
        )
        signup_button.click()

        # Wait for the URL to change to the login page
        WebDriverWait(driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/login/")
        )
        print("Test Case 2: Signup successful and redirected to login page")

    except Exception as e:
        print(f"Test Case 2: Signup failed due to {str(e)}")

time.sleep(3)
def login_test():
    try:
       
        print("Attempting to log in...")

        # Fill in the Username field
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form/input[2]"))
        )
        username_input.clear()
        username_input.send_keys("Khadiza")

        # Fill in the Password field
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/form/input[3]"))
        )
        password_input.clear()
        password_input.send_keys("12345")

        # Click the Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/form/input[4]"))
        )
        login_button.click()


        WebDriverWait(driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/home/")
        )
        print("Test Case 3: Login successful and redirected to Home page")

    except Exception as e:
        print(f"Test Case 3: Login failed due to {str(e)}")     




# Run the tests
try:
    test_navigate_to_homepage()
    signup_test()
    login_test()


    print("All tests completed. The browser will remain open for inspection.")
    input("Press Enter to close the browser...")  

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()
