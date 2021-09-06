import logging

from database.api_db import (get_all_categories, get_all_plates, get_user,
                             get_user_step, make_keyboard, update_user)
from utils.constants import TOKEN
from utils.tools import normalize_text

import telebot
from telebot import apihelper

apihelper.SESSION_TIME_TO_LIVE = 5 * 60

logger = telebot.logger
telebot.logger.setLevel(logging.ERROR)

bot = telebot.TeleBot(TOKEN)


# handle the "/start" command
@bot.message_handler(commands=['start'],
                     func=lambda message: get_user_step(message) == 0.0)
def command_start_new_user(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    msg = bot.send_message(cid, 'Olá! Posso te chamar de {}?'.format(
        m.chat.first_name), reply_markup=make_keyboard('pgt_sim_nao'))
    bot.register_next_step_handler(msg, process_name)


def process_name(m):
    cid = m.chat.id
    answer = m.text
    if answer == 'Sim':
        update_user(m, name=m.chat.first_name,
                    step=1.0, unknown=False)
        bot.send_chat_action(cid, 'typing')
        bot.reply_to(
            m, 'Bem vindo, {}!'.format(
                get_user(m)['name']))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid, 'Como posso te ajudar?',
            reply_markup=make_keyboard('menu_principal'))
    elif answer == 'Não':
        bot.send_chat_action(cid, 'typing')
        msg = bot.send_message(cid, 'Então, como gostaria de ser chamado?')
        bot.register_next_step_handler(msg, take_name)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.reply_to(m, 'Por favor, responda Sim ou Não.')
        bot.send_chat_action(cid, 'typing')
        msg = bot.send_message(cid, 'Posso te chamar de {}?'.format(
            m.chat.first_name), reply_markup=make_keyboard(
                'pgt_sim_nao'))
        bot.register_next_step_handler(msg, process_name)


def take_name(m):
    cid = m.chat.id
    update_user(m, name=m.text,
                step=1.0, unknown=False)
    bot.send_chat_action(cid, 'typing')
    bot.send_message(
        cid, 'Bem vindo, {}!'.format(
            get_user(m)['name']))
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, 'Posso te ajudar?')


@bot.message_handler(commands=['start'],
                     func=lambda message: get_user_step(message) == 1.0)
def command_start(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    bot.send_message(
        cid, 'Olá, {}! Tudo bem?'.format(
            get_user(m)['name']))
    bot.send_chat_action(cid, 'typing')
    bot.send_message(
        cid, 'Como posso te ajudar?',
        reply_markup=make_keyboard('menu_principal'))


@bot.message_handler(
    func=lambda message: normalize_text(message.text) == 'cardapio')
def take_category(m):
    cid = m.chat.id
    update_user(m, step=2.0)
    bot.send_chat_action(cid, 'typing')
    msg = bot.reply_to(
        m, 'Qual categoria gostaria de ver?',
        reply_markup=make_keyboard(_keyboard={
            'name': 'categories',
            'footer': ['Voltar'],
            'body': get_all_categories()
        }))
    bot.register_next_step_handler(msg, take_plate)


def take_plate(m):
    cid = m.chat.id
    cat = m.text
    bot.send_chat_action(cid, 'typing')
    msg = bot.send_message(
        cid, '{}, temos as seguintes opções nesta categoria.'.format(
            get_user(m)['name']), reply_markup=make_keyboard(_keyboard={
                'name': cat,
                'footer': ['Voltar'],
                'body': get_all_plates(cat)
            }))
    bot.register_next_step_handler(msg, process_plate)


def process_plate(m):
    ...


bot.polling()
