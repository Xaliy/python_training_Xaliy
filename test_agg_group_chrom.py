# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest  #, time, re


class UntitledTestCase(unittest.TestCase):
	def setUp(self):
		# self.wd = webdriver.Chrome(executable_path=r'')
		self.wd = webdriver.Chrome()
		self.wd.implicitly_wait(100)
		# self.base_url = "https://www.google.com/"
		# self.verificationErrors = []
		# self.accept_next_alert = True

	def test_untitled_test_case(self):
		wd = self.wd
		# driver.get(self.base_url + "chrome://newtab/")
		wd.get("http://localhost/addressbook/")
		wd.find_element_by_name("user").click()
		wd.find_element_by_name("user").clear()
		wd.find_element_by_name("user").send_keys("admin")
		wd.find_element_by_name("pass").click()
		wd.find_element_by_name("pass").clear()
		wd.find_element_by_name("pass").send_keys("secret")
		wd.find_element_by_id("LoginForm").click()
		wd.find_element_by_xpath("//input[@value='Login']").click()
		wd.find_element_by_link_text("groups").click()
		wd.find_element_by_name("new").click()
		wd.find_element_by_name("group_name").click()
		wd.find_element_by_name("group_name").clear()
		wd.find_element_by_name("group_name").send_keys("new_group2")
		wd.find_element_by_name("group_header").click()
		wd.find_element_by_name("group_header").clear()
		wd.find_element_by_name("group_header").send_keys("heder_group")
		wd.find_element_by_name("group_footer").click()
		wd.find_element_by_name("group_footer").clear()
		wd.find_element_by_name("group_footer").send_keys("footer_group")
		wd.find_element_by_name("submit").click()
		wd.find_element_by_link_text("group page").click()
		wd.find_element_by_link_text("Logout").click()

	# ERROR: Caught exception [unknown command []]
	# ERROR: Caught exception [unknown command []]

	def is_element_present(self, how, what):
		try:
			self.wd.find_element(by=how, value=what)
		except NoSuchElementException as e:
			return False
		return True

	def is_alert_present(self):
		try:
			self.wd.switch_to_alert()
		except NoAlertPresentException as e:
			return False
		return True


	def tearDown(self):
		self.wd.quit()


if __name__ == "__main__":
	unittest.main()
