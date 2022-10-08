import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_Admin01_SearchEmployeeUsername_Positive(self):
        # login
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
        # Admin
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "searchSystemUser_userName").send_keys(
            "Admin")
        driver.find_element(By.ID, "searchBtn").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        self.assertEqual(response_message, 'Admin')

    def test_Admin02_FindNonEmployeeUsername_Negative(self):
        # login
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
        # Admin
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "searchSystemUser_userName").send_keys(
            "Nando")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response_message, 'No Records Found')

    def test_Admin03_AddUsedUsername_Negative(self):
        # login
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
        # Admin
        time.sleep(3)
        driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys(
            "Alice")
        driver.find_element(By.ID, "btnSave").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text


unittest.main()
