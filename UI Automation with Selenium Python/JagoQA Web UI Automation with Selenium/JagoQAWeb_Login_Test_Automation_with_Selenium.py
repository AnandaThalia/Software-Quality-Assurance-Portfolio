import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("jagoqaindonesia@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Welcome Jago QA")
        self.assertEqual(respon_berhasil, "Anda Berhasil Login")

    def test_b_failed_login_email_not_registered(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertIn("not found", respon_welcome)
        self.assertIn("Salah", respon_berhasil)
        self.assertEqual(respon_welcome, "User\'s not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")
        #

    def test_c_failed_login_empty_email_and_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, "Gagal Login!")

    def test_d_failed_login_empty_email(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, "Gagal Login!")

    def test_e_failed_login_empty_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "User\'s not found")
        self.assertEqual(respon_berhasil, "Email atau Password Anda Salah")

    def test_f_failed_login_email_too_long(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("wxsmgswoylgxmgeqzkongnlpghkxlulahcvdamudbypfwlbkizmfwvezbmebxtexnqhxanpcibddolrxgswtnhaavwseabkxjvmdmlaenjria@jagoqa.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("sman60jakarta")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, "Gagal Login!")

    def test_g_failed_login_password_too_long(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "wxsmgswoylgxmgeqzkongnlpghkxlulahcvdamudbypfwlbkizmfwvezbmebxtexnqhxanpcibddolrxgswtnhaavwseabkxjvmdmlaenjria")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, "Gagal Login!")


#     #Belum berhasil catch error
#     def test_h_failed_login_invalid_email_format(self):
#         driver = self.driver
#         driver.get("http://barru.pythonanywhere.com/daftar")
#         time.sleep(1)
#         driver.find_element(
#             By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("nanda@@jagoqa.com")
#         time.sleep(1)
#         driver.find_element(By.ID, "password").send_keys("wxsmgswoylgxmgeqzk")
#         time.sleep(1)
#         driver.find_element(
#             By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
#         time.sleep(2)
#         respon_welcome = driver.find_element(
#             By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
#         respon_berhasil = driver.find_element(
#             By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
#         self.assertEqual(respon_welcome, "Oops...")
#         self.assertEqual(respon_berhasil, "Gagal Login!")

    def test_i_failed_login_password_contain_symbol(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("nanda@jagoqa.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("wxsmgsw&@jria")
        time.sleep(1)
        driver.find_element(
            By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)
        respon_welcome = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        respon_berhasil = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(respon_welcome, "Oops...")
        self.assertEqual(respon_berhasil, "Gagal Login!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
