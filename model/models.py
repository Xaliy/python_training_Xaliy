from sys import maxsize


class Group:
    """Класс описывающий группу и ее свойства."""

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        # return "%s:%s" % self.id, self.name
        return f'{self.id}:{self.name}'

    def __eq__(self, other):
        return ((self.id is None or other.id is None or
                 self.id == other.id) and self.name == other.name
                )

    def if_or_max(self):
        """Метод сравнения списка по ключу ID."""
        if self.id:
            return int(self.id)
        return maxsize


class Contact:
    """Класс описывающий Контакт и его свойства."""

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, title=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_gmail_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        # self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home  # работаем с этим полем
        self.phone_mobile = phone_mobile  # работаем с этим полем
        self.phone_work = phone_work  # работаем с этим полем
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2  # работаем с этим полем
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_gmail_from_home_page = all_gmail_from_home_page

    def __repr__(self):
        return f'{self.id}:{self.firstname}, {self.lastname}'

    def __eq__(self, other):
        return ((self.id is None or other.id is None or
                 self.id == other.id)
                and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def if_or_max(self):
        """Метод сравнения списка по ключу ID."""
        if self.id:
            return int(self.id)
        return maxsize
