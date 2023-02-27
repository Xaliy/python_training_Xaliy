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
        return f'{self.id}: {self.name}, {self.header}, {self.footer}'

    def __eq__(self, other):
        return ((
             self.id is None or other.id is None
             or self.id == other.id)
                and (self.name == other.name
                     or self.name is None
                     or other.name is None)
                and (self.header == other.header
                     or self.header is None
                     or other.header is None)
                and (self.footer == other.footer
                     or self.footer is None
                     or other.footer is None)
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
            phone_home=None, phone_mobile=None, phone_work=None, fax=None,
            email=None, email2=None, email3=None, homepage=None, bday=None,
            bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
            address2=None, phone2=None, notes=None, id=None,
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
        return f'''{self.id}:{self.firstname}, {self.lastname},
                    {self.company}, {self.address}'''

    def __eq__(self, other):
        return ((
            self.id is None or other.id is None
            or self.id == other.id)
                and (self.firstname == other.firstname
                     or self.firstname is None
                     or other.firstname is None)
                and (self.lastname == other.lastname
                     or self.lastname is None
                     or other.lastname is None)
                and (self.middlename == other.middlename
                     or self.middlename is None
                     or other.middlename is None)
                and (self.nickname == other.nickname
                     or self.nickname is None
                     or other.nickname is None)
                # self.photo = photo
                and (self.title == other.title
                     or self.title is None
                     or other.title is None)
                and (self.company == other.company
                     or self.company is None
                     or other.company is None)
                and (self.address == other.address
                     or self.address is None
                     or other.address is None)
                and (self.phone_home == other.phone_home
                     or self.phone_home is None
                     or other.phone_home is None)
                and (self.phone_mobile == other.phone_mobile
                     or self.phone_mobile is None
                     or other.phone_mobile is None)
                and (self.phone_work == other.phone_work
                     or self.phone_work is None
                     or other.phone_work is None)
                and (self.fax == other.fax
                     or self.fax is None
                     or other.fax is None)
                and (self.email == other.email
                     or self.email is None
                     or other.email is None)
                and (self.email2 == other.email2
                     or self.email2 is None
                     or other.email2 is None)
                and (self.email3 == other.email3
                     or self.email3 is None
                     or other.email3 is None)
                and (self.homepage == other.homepage
                     or self.homepage is None
                     or other.homepage is None)
                and (self.bday == other.bday
                     or self.bday is None
                     or other.bday is None)
                and (self.bmonth == other.bmonth
                     or self.bmonth is None
                     or other.bmonth is None)
                and (self.byear == other.byear
                     or self.byear is None
                     or other.byear is None)
                and (self.aday == other.aday
                     or self.aday is None
                     or other.aday is None)
                and (self.amonth == other.amonth
                     or self.amonth is None
                     or other.amonth is None)
                and (self.ayear == other.ayear
                     or self.ayear is None
                     or other.ayear is None)
                and (self.address2 == other.address2
                     or self.address2 is None
                     or other.address2 is None)
                and (self.phone2 == other.phone2
                     or self.phone2 is None
                     or other.phone2 is None)
                and (self.notes == other.notes
                     or self.notes is None
                     or other.notes is None)
        )

    def if_or_max(self):
        """Метод сравнения списка по ключу ID."""
        if self.id:
            return int(self.id)
        return maxsize
