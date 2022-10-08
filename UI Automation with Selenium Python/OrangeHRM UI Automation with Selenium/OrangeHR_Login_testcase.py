import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Login1_Positif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys(
            "Admin")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "admin123")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(
            By.ID, "menu_admin_viewAdminModule").text
        self.assertEqual(response_message, 'Admin')

    def test_Login2_WrongUsernameWithCorrectPassword_Negatif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys(
            "admiin")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "admin123")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')

    def test_Login3_CorrectUsernameAndWrongPassword_Negatif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys(
            "Admin")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "admin1234")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')

    def test_Login4_EmptyUsernameAndCorrectPassword_Negatif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys("")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "admin123")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, 'Username cannot be empty')

    def test_Login5_CorrectUsernameAndEmptyPassword_Negatif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys(
            "Admin")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, 'Password cannot be empty')

    def test_Login6_EmptyUsernameWithEmptyPassword_Negatif(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")  # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys("")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys(
            "")  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, 'Username cannot be empty')


unittest.main()
