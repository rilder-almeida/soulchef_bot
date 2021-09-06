from factory.headers import (client_header, keyboard_header, menu_header,
                             message_header, user_header)
from tinysheet.tinysheet import TinySheet

default_db = TinySheet('default.json')
user_db = TinySheet('user.json')

keyboard_table = default_db.sheet(
    'keyboard', allow_unknown=False, header=keyboard_header)

message_table = default_db.sheet(
    'message', allow_unknown=True, header=message_header)

menu_table = default_db.sheet(
    'menu', allow_unknown=True, header=menu_header)

user_table = user_db.sheet(
    'user', allow_unknown=True, purge_unknown=True,
    header=user_header)

client_table = user_db.sheet(
    'client', allow_unknown=True,  purge_unknown=True,
    header=client_header)
