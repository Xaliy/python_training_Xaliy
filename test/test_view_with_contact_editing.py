# -*- coding: utf-8 -*-
import re
from random import randrange


def _clear_phone(s):
    """Функция очистки символов для телефона."""
    return re.sub('[() -]', '', s)


def _clear_surplus_spaces(s):
    """Функция очистки двйных, лидирующих и концевых пробелов."""
    return re.sub(r'^\s+', ' ', s).strip()


def _merge_phones_like_on_home_page(contact):
    """Функция склеивания телефонов в одну строку без пробелов и символов."""
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: _clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home,
                                        contact.phone_mobile,
                                        contact.phone_work,
                                        contact.phone2]))))


def _merge_email_like_on_home_page(contact):
    """Функция склеивания email в одну строку без пробелов и символов."""
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: _clear_surplus_spaces(x),
                                filter(lambda x: x is not None,
                                       [contact.email,
                                        contact.email2,
                                        contact.email3]))))


def test_compare_contact_homepage_with_editing(app):
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_from_homepage_page = (app.contact.get_contact_from_homepage_page(
                                                index))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert (contact_from_homepage_page.firstname ==
            _clear_surplus_spaces(contact_from_edit_page.firstname))
    assert (contact_from_homepage_page.lastname ==
           _clear_surplus_spaces(contact_from_edit_page.lastname))
    assert (contact_from_homepage_page.address ==
            _clear_surplus_spaces(contact_from_edit_page.address))
    # assert (_clear(contact_from_homepage_page.email) ==
    #         _clear(contact_from_edit_page.email))
    assert (contact_from_homepage_page.all_gmail_from_home_page ==
            _merge_email_like_on_home_page(contact_from_edit_page))
    assert (contact_from_homepage_page.all_phones_from_home_page ==
            _merge_phones_like_on_home_page(contact_from_edit_page))
