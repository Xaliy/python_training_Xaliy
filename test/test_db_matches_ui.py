from model.models import Group
from timeit import timeit


def test_group_list(app, db):
    """Вызов данных из БД и данных в браузере. Время обработки"""
    # провыеряем скорость выполнения формирования списков
    print()
    print('интерфейс: ', timeit(lambda: app.group.get_group_list(), number=1))
    ui_list = app.group.get_group_list()

    def _clean_gr(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(_clean_gr, db.get_group_list_db())
    print('БД: ', timeit(lambda: map(_clean_gr, db.get_group_list_db()),
                        number=1000))
    # assert False  # что бы тест упал и был вывод в консоль
    assert (sorted(ui_list, key=Group.if_or_max) ==
            sorted(db_list, key=Group.if_or_max))


    # def test_group_list_old(app, db):
    # """Сравнение данных из БД и данных в браузере"""
    # ui_list = app.group.get_group_list()
    #
    # def _clean_gr_o(group):
    #     return Group(id=group.id, name=group.name.strip())
    # db_list = map(_clean_gr_o, db.get_group_list())
    # assert (sorted(ui_list, key=Group.if_or_max) ==
    #         sorted(db_list, key=Group.if_or_max))
    #
