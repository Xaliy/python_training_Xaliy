# -*- coding: utf-8 -*-
import re


def clear(s):
    return re.sub("[() -]", "", s)


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # сравниваем
    assert contact_from_home_page.phone_home == clear(
            contact_from_edit_page.phone_home)
    assert contact_from_home_page.phone_work == clear(
            contact_from_edit_page.phone_work)
    assert contact_from_home_page.phone_mobile == clear(
            contact_from_edit_page.phone_mobile)
    assert contact_from_home_page.phone2 == clear(
            contact_from_edit_page.phone2)


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
