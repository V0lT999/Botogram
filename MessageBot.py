#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import json

PROOFIT_BOT = "Proofit_test_bot"

with open('Tokens.json') as json_file:
    tokens = json.loads(json_file.read())
bot = telebot.TeleBot(tokens[PROOFIT_BOT])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "All right!")
    elif message.text == "go":
        # id = bot.get_chat(message.from_user.id).id
        id = message.from_user.id
        bot.send_message(message.from_user.id, "message_id: {}".format(id))
    else:
        bot.send_message(message.from_user.id, "I don't understand! Please write /help.")


bot.polling(none_stop=True, interval=0)
