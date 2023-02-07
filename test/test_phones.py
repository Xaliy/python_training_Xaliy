# -*- coding: utf-8 -*-
import re


def _clear(s):
    """Функция очистки символов."""
    return re.sub("[() -]", "", s)


def _merge_phones_like_on_home_page(contact):
    """Функция склеивания телефонов в одну строку без пробелов и символов."""
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: _clear(x),
                                filter(lambda x: x is not None,
                                       [contact.phone_home,
                                        contact.phone_mobile,
                                        contact.phone_work,
                                        contact.phone2]))))


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # сравниваем
    assert (contact_from_home_page.all_phones_from_home_page ==
            _merge_phones_like_on_home_page(contact_from_edit_page))
    #
    # assert contact_from_home_page.phone_home == _clear(
    #         contact_from_edit_page.phone_home)
    # assert contact_from_home_page.phone_work == _clear(
    #         contact_from_edit_page.phone_work)
    # assert contact_from_home_page.phone_mobile == _clear(
    #         contact_from_edit_page.phone_mobile)
    # assert contact_from_home_page.phone2 == _clear(
    #         contact_from_edit_page.phone2)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert (contact_from_view_page.phone_home ==
           contact_from_edit_page.phone_home)
    assert (contact_from_view_page.phone_work ==
            contact_from_edit_page.phone_work)
    assert (contact_from_view_page.phone_mobile ==
            contact_from_edit_page.phone_mobile)
    assert (contact_from_view_page.phone2 ==
            contact_from_edit_page.phone2)
