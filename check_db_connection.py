# 2 вариант проверки соединения с БД через объект, и вывод на консоль
from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name="addressbook",
               user="root", password="")

try:
    groups = db.get_group_list_db()
finally:
    db.destroy()

# 1 вариант
# import pymysql.cursors
#
# connection = pymysql.connect(host="127.0.0.1", database="addressbook",
#                              user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
