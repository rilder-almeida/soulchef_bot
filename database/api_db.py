from database.tables import keyboard_table, menu_table, user_table
from factory.keyboards import keyboard_factory

from telebot import types


# user
def get_user_model(data: dict):
    return user_table.model(data=data)


def check_user(message) -> bool:
    return user_table.contains(
        user_table.where.uid == message.chat.id)


def get_user(message) -> dict:
    if check_user(message):
        return user_table.get(
            user_table.where.uid == message.chat.id)
    else:
        return None


def update_user(message, key=None, value=None, **kwargs):
    if check_user(message):
        user = get_user(message)
        if key is not None and value is not None:
            user.update({key: value})
        if kwargs:
            user.update(kwargs)
        user_model = user_table.model()
        user = user_model(**user)
        user_table.upsert(
            user.validated(), user_table.where.uid == message.chat.id)
    else:
        add_user(message)
        update_user(message, key, value)


def add_user(message) -> dict:
    user_model = user_table.model()
    user = user_model(uid=message.chat.id, step=0.0, unknown=True)
    user_table.insert(user.validated())
    return get_user(message)


def get_user_step(message) -> float:
    if check_user(message):
        return get_user(message)['step']
    else:
        return add_user(message)['step']


def set_user_step(message, step: float):
    get_user(message)['step'].update(step)


# keyboard
hideBoard = (types.ReplyKeyboardRemove())


def get_keyboard_model(data: dict):
    return keyboard_table.model(data=data)


def get_keyboard(name: str) -> dict:
    return keyboard_table.get(
        keyboard_table.where.name == name) if keyboard_table.contains(
            keyboard_table.where.name == name) else None


def add_keyboard(_keyboard):
    keyboard = get_keyboard_model(_keyboard)
    keyboard_table.insert(keyboard.validated())


def make_keyboard(name: str = None, *, _keyboard=None):
    if name is not None and keyboard_table.contains(
            keyboard_table.where.name == name):
        return keyboard_factory(get_keyboard(name))
    elif name is None and _keyboard is not None:
        keyboard = get_keyboard_model(_keyboard)
        return keyboard_factory(keyboard.validated())
    else:
        return None


def get_category(name: str) -> dict:
    return menu_table.get(
        menu_table.where.name == name) if menu_table.contains(
        menu_table.where.name == name) else None


def get_all_categories() -> list:
    result = []
    for c in menu_table.all():
        result.append(c['name'])
    return result


def get_plate(plate: str, category: str) -> dict:
    category = menu_table.get(
        menu_table.where.name == category) if menu_table.contains(
        menu_table.where.name == category) else None

    if category is not None:
        return category.get(
            category.where.name == plate) if category.contains(
            category.where.name == plate) else None
    else:
        return None


def get_all_plates(category: str) -> list:
    return list(get_category(category)['plates'].keys())


def add_category():
    pass


def add_plate():
    pass


def del_category():
    pass


def del_plate():
    pass
