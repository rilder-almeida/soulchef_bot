from telebot.types import ReplyKeyboardMarkup
from utils.tools import to_string


def keyboard_factory(keyboard: dict, **kwargs) -> ReplyKeyboardMarkup:
    _kb = ReplyKeyboardMarkup(
        resize_keyboard=keyboard['resize'],
        one_time_keyboard=keyboard['once'],
        **kwargs
    )

    _parsed_header = []
    if isinstance(keyboard['header'], list) and keyboard['header'] != []:
        for item in keyboard['header']:
            if not isinstance(item, list):
                item = [item]
            _parsed_header.append(item)

    _parsed_body = []
    if isinstance(keyboard['body'], list) and keyboard['body'] != []:
        for item in keyboard['body']:
            if not isinstance(item, list):
                item = [item]
            _parsed_body.append(item)

    _parsed_footer = []
    if isinstance(keyboard['footer'], list) and keyboard['footer'] != []:
        for item in keyboard['footer']:
            if not isinstance(item, list):
                item = [item]
            _parsed_footer.append(item)

    for buttons in [*_parsed_header, *_parsed_body, *_parsed_footer]:
        _row_buttons = []
        for b in buttons:
            _row_buttons.append(to_string(b))
        _kb.row(*_row_buttons)

    return _kb
