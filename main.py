import telebot
import requests
import time
import configparser
import os

config = configparser.ConfigParser()
config.read('miro_bot.cfg')

bot = telebot.TeleBot(config.get("tg", "token"))


def send_file(file):
    with open("image.jpg", 'wb') as new_file:
        new_file.write(file)

    url = "https://api.miro.com/v2/boards/" + config.get("miro", "board") + "/images"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer" + config.get("miro", "token")
    }
    rbfile = open('image.jpg', 'rb')
    files = {
        'resource': ('image.jpg', rbfile, 'image/jpg'),
    }
    response = requests.post(url, headers=headers, files=files)
    print(response.text)
    print(response.request.body)

    rbfile.close()
    os.remove('image.jpg')


@bot.message_handler(content_types=['photo'])
def photo(message):
    fileid = message.photo[-1].file_id
    file = bot.get_file(fileid)
    downloaded_file = bot.download_file(file.file_path)
    send_file(downloaded_file)
    bot.reply_to(message, "yep")


@bot.message_handler(func=lambda message: message.document.mime_type == 'image/png' or message.document.mime_type == 'image/jpg', content_types=['document'])
def handle_document(message):
    fileid = message.document.file_id
    file = bot.get_file(fileid)
    downloaded_file = bot.download_file(file.file_path)
    send_file(downloaded_file)
    bot.reply_to(message, "yep")


if __name__ == '__main__':
    while True:
        try:
            print("Server up")
            bot.polling()
        except ConnectionError:
            print("Server down: ConnectionError")
            time.sleep(5)
            continue
