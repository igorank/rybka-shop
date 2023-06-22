import sqlite3
import random
from tgbot.data.config import PATH_DATABASE
from tgbot.utils.const_functions import get_date, clear_html


# Преобразование полученного списка в словарь
def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict


def add_itemx(category_id, position_id, get_all_items, user_id, user_name):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory

        for item_data in get_all_items:
            # if not item_data.isspace() and item_data != "":
            con.execute("INSERT INTO storage_item "
                        "(item_id, item_data, position_id, category_id, creator_id, creator_name, add_date) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)",
                        [random.randint(1000000000, 9999999999), clear_html(item_data.strip()), position_id,
                         category_id,
                         user_id, user_name, get_date()])


if __name__ == '__main__':
    with open('1.txt', 'r') as file:
        lines = file.readlines()

    add_itemx(1686952519, 1687340755, lines, 2031127410, "Igor")

