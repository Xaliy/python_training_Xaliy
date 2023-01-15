from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:
	def __init__(self):
		# self.wd = webdriver.Firefox()
		# self.wd.implicitly_wait(100)
		self.wd = WebDriver()
		self.wd.implicitly_wait(100)
		self.session = SessionHelper(self)
		
	def open_home_page(self):
		wd = self.wd
		# open home page
		wd.get('http://localhost/addressbook/')

	def return_to_groups_page(self):
		wd = self.wd
		wd.find_element_by_link_text('group page').click()
		
	def create_group(self, group):
		wd = self.wd
		self.open_groups()
		# init group creation
		wd.find_element_by_name("new").click()
		# fill group form
		wd.find_element_by_name("group_name").click()
		wd.find_element_by_name("group_name").clear()
		wd.find_element_by_name("group_name").send_keys(group.name)
		wd.find_element_by_name("group_header").click()
		wd.find_element_by_name("group_header").clear()
		wd.find_element_by_name("group_header").send_keys(group.header)
		wd.find_element_by_name("group_footer").click()
		wd.find_element_by_name("group_footer").clear()
		wd.find_element_by_name("group_footer").send_keys(group.footer)
		# submit group creation
		wd.find_element_by_name("submit").click()
		self.return_to_groups_page()
		
	def open_groups(self):
		wd = self.wd
		# open group page
		wd.find_element_by_link_text("groups").click()
		
		
	def return_to_home_page(self):
		wd = self.wd
		# home page
		wd.find_element_by_link_text('home').click()
		
	def open_form_new_contact(self):
		wd = self.wd
		wd.find_element_by_link_text('add new').click()
	
	def create_new_contact(self, contact):
		"""
		Добавляем новый контакт.
		Заполняем поля формы и сохраняем.
		"""
		wd = self.wd
		self.open_form_new_contact()
		# text fields
		wd.find_element_by_name('firstname').click()
		wd.find_element_by_name('firstname').clear()
		wd.find_element_by_name('firstname').send_keys(contact.firstname)
		wd.find_element_by_name('middlename').click()
		wd.find_element_by_name('middlename').clear()
		wd.find_element_by_name('middlename').send_keys(contact.middlename)
		wd.find_element_by_name('lastname').click()
		wd.find_element_by_name('lastname').clear()
		wd.find_element_by_name('lastname').send_keys(contact.lastname)
		wd.find_element_by_name('nickname').click()
		wd.find_element_by_name('nickname').clear()
		wd.find_element_by_name('nickname').send_keys(contact.nickname)
		# wd.find_element_by_name("photo").click()
		wd.find_element_by_name('title').click()
		wd.find_element_by_name('title').clear()
		wd.find_element_by_name('title').send_keys(contact.title)
		wd.find_element_by_name('company').click()
		wd.find_element_by_name('company').clear()
		wd.find_element_by_name('company').send_keys(contact.company)
		wd.find_element_by_name('address').click()
		wd.find_element_by_name('address').clear()
		wd.find_element_by_name('address').send_keys(contact.address)
		wd.find_element_by_name('home').click()
		wd.find_element_by_name('home').clear()
		wd.find_element_by_name('home').send_keys(contact.phone_home)
		wd.find_element_by_name('mobile').click()
		wd.find_element_by_name('mobile').clear()
		wd.find_element_by_name('mobile').send_keys(contact.phone_mobile)
		wd.find_element_by_name('work').click()
		wd.find_element_by_name('work').clear()
		wd.find_element_by_name('work').send_keys(contact.phone_work)
		wd.find_element_by_name('fax').click()
		wd.find_element_by_name('fax').clear()
		wd.find_element_by_name('fax').send_keys(contact.fax)
		wd.find_element_by_name('email').click()
		wd.find_element_by_name('email').clear()
		wd.find_element_by_name('email').send_keys(contact.email)
		wd.find_element_by_name('email2').click()
		wd.find_element_by_name('email2').clear()
		wd.find_element_by_name('email2').send_keys(contact.email2)
		wd.find_element_by_name('email3').click()
		wd.find_element_by_name('email3').clear()
		wd.find_element_by_name('email3').send_keys(contact.email3)
		wd.find_element_by_name('homepage').click()
		wd.find_element_by_name('homepage').clear()
		wd.find_element_by_name('homepage').send_keys(contact.homepage)
		wd.find_element_by_name('bday').click()
		# calendars
		wd.find_element_by_xpath('//option[@value="' + contact.bday +
								 '"]').click()
		wd.find_element_by_name('bmonth').click()
		wd.find_element_by_xpath('//option[@value="' + contact.bmonth +
								 '"]').click()
		wd.find_element_by_name('byear').click()
		wd.find_element_by_name('byear').clear()
		wd.find_element_by_name('byear').send_keys(contact.byear)
		wd.find_element_by_name('aday').click()
		wd.find_element_by_xpath(
				'//div[@id="content"]/form/select[3]/option[3]').click()
		wd.find_element_by_name('amonth').click()
		wd.find_element_by_xpath(
				'//div[@id="content"]/form/select[4]/option[2]').click()
		# text fields
		wd.find_element_by_name('ayear').click()
		wd.find_element_by_name('ayear').clear()
		wd.find_element_by_name('ayear').send_keys(contact.ayear)
		wd.find_element_by_name('address2').click()
		wd.find_element_by_name('address2').clear()
		wd.find_element_by_name('address2').send_keys(contact.address2)
		wd.find_element_by_name('phone2').click()
		wd.find_element_by_name('phone2').clear()
		wd.find_element_by_name('phone2').send_keys(contact.phone2)
		wd.find_element_by_name('notes').click()
		wd.find_element_by_name('notes').clear()
		wd.find_element_by_name('notes').send_keys(contact.notes)
		# save
		wd.find_element_by_xpath(
				'//div[@id="content"]/form/input[21]').click()
		self.return_to_home_page()
	
	def destroy(self):
		self.wd.quit()
