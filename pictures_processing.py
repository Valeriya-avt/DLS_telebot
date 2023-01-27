import model
import telebot
from datetime import datetime 
from telebot import types


def log(text):
    time_stamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    print(time_stamp + " " + text)


with open("creds/ChangeImageStyle_bot.txt", "r") as f:
    change_image_style_creds = f.read().strip()

def style_transfer(message, style_image, content_image):
    new_image = model.process(style_image, content_image)

    log("OK")

    bot = telebot.TeleBot(change_image_style_creds)
    bot.send_photo(message.from_user.id, photo=new_image)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(back)
    bot.send_message(message.from_user.id, "Готово!", reply_markup=markup)
    bot.close()
