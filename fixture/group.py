class GroupHelper:
	"""класс описывающий фикстуры объекта группа."""
	
	def __init__(self, app):
		self.app = app

	def open_groups(self):
		"""Открыть форму создания новой группы."""
		wd = self.app.wd
		# open group page
		wd.find_element_by_link_text("groups").click()

	def create(self, group):
		"""
		Вызов метода открытия формы для создания новой группы.
		Фикстура заполнения полей формы группа и сохранения.
		Вызыв метода переход на страницу со списком групп.
		"""
		wd = self.app.wd
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

	def return_to_groups_page(self):
		"""Переход на страницу со списком групп"""
		wd = self.app.wd
		wd.find_element_by_link_text('group page').click()