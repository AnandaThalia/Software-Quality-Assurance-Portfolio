import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestPIM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_PIM1_SearchEmployeeName_Positive(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(5)
        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(
            "Admin")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td[3]/a").text
        self.assertEqual(response_message, 'Admin')

    def test_PIM2_SearchNonEmployeName_Negative(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(5)
        driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(
            "Nando")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response_message, 'No Records Found')

    def test_PIM3_SearchNonEmpolyeeID_Negative(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "empsearch_id").send_keys(
            "1272")
        driver.find_element(By.ID, "searchBtn").click()
        time.sleep(5)
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual(response_message, 'No Records Found')

    def test_PIM4_AddEmployee_Positive(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID, "firstName").send_keys(
            "Ananda")
        driver.find_element(By.ID, "lastName").send_keys(
            "Thalia")
        driver.find_element(By.ID, "btnSave").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/h1").text
        self.assertEqual(response_message, 'Personal Details')

    def test_PIM5_AddEmployeeWithEmptyLastName_Negative(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID, "firstName").send_keys(
            "Ananda")
        driver.find_element(By.ID, "lastName").send_keys(
            "")
        driver.find_element(By.ID, "btnSave").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text
        self.assertEqual(response_message, 'Required')

    def test_PIM6_AddEmployeeWithEmptyFirstName_Negative(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID, "firstName").send_keys(
            "")
        driver.find_element(By.ID, "lastName").send_keys(
            "Thalia")
        driver.find_element(By.ID, "btnSave").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[1]/span").text
        self.assertEqual(response_message, 'Required')
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text
        self.assertEqual(response_message, 'Required')

    def test_PIM7_AddEmployeeWithEmptyFirstLastname_Negative(self):
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
        # PIM
        time.sleep(3)
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        time.sleep(3)
        driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID, "firstName").send_keys(
            "")
        driver.find_element(By.ID, "lastName").send_keys(
            "")
        driver.find_element(By.ID, "btnSave").click()
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[1]/span").text
        self.assertEqual(response_message, 'Required')
        response_message = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text
        self.assertEqual(response_message, 'Required')


unittest.main()
