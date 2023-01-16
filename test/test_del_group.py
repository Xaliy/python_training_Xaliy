def test_delete_first_group(app):
	"""Тест удаляем первую группу в списке."""
	app.session.login(username='admin', password='secret')
	app.group.delete_first_group()
	app.session.logaut_website()
