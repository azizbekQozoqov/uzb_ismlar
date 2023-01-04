from finder import get_name, search_name, get_footer
from appdb import get_all_users, add_user, add_message
from telebot import TeleBot
from telebot.types import Message
import telebot
import os
from flask import Flask, request



TOKEN="5952434127:AAF1hA0ikhVSzqI1yB-ynuzRX7YXk-EIcK0"
bot = TeleBot(TOKEN)



server = Flask(__name__)



@bot.message_handler(commands=["start"])
def start(msg: Message):
    add_user(msg)
    bot.reply_to(msg, "Done")


@bot.message_handler(func=lambda msg: True)
def ret(msg: Message):
    add_user(msg)
    data = get_name(msg.text)
    if data["ok"] == True:
        txt= f"""✅ <b>{msg.text.title()}</b>\n\n{data['meaning']}\n\n<code>{data['desc']}</code>\n\n{get_footer()}"""
        bot.send_message(msg.from_user.id, txt, parse_mode="HTML")
        add_message(msg, True)
    else:
        add_message(msg, False)
        return bot.reply_to(msg, data["message"])

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get("SITENAME") + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))