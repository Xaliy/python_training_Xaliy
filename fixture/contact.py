class ContactHelper:
	"""фикстуры объекта контакт"""
	
	def __init__(self, app):
		self.app = app

	def open_form_new_contact(self):
		"""Открываем форму для моздания нового контакта."""
		wd = self.app.wd
		wd.find_element_by_link_text('add new').click()

	def return_to_home_page(self):
		"""Переходим на домашную страницу."""
		wd = self.app.wd
		# home page
		wd.find_element_by_link_text('home').click()

	def create_new_contact(self, contact):
		"""
		Вызов метода открытия формы создания нового контакта.
		Добавляем новый контакт.
		Заполняем поля формы и сохраняем.
		Вызов метода перехода на домашную страницу.
		"""
		wd = self.app.wd
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
		
