import telebot
from config import TOKEN
# from pixivBot.main import main
from weather import *
import datetime
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "狗东西你好 我是CorgiBot")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_info = '''
    天气查询: /weather 城市名
    '''
    bot.reply_to(message, help_info)

@bot.message_handler(commands=['weather'])
def get_weather(message):
    print("* Weather Request: ", message)
    city = message.text
    city = city.replace('/weather', '').strip()
    print("查询城市:", city)
    status, weather_info = get_info(city)
    print(status, weather_info)
    if status == -1:
        bot.reply_to(message, "你这个xjb输的城市名老子找不到啊？你再试试？")
        bot.send_sticker(message.chat.id, 'CAADBQADQAADvXbGBbm8R2q8xH5QAg')
    else:
        bot.reply_to(message, weather_info)
        bot.send_sticker(message.chat.id, 'CAADBQADCAADvXbGBYdALs5Bu1fNAg')

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    print(message)
    print("Sticker id Get:", message.sticker.file_id)
    bot.reply_to(message, f"想必你就是{message.from_user.first_name}吧。我日！是表情包！")
    bot.reply_to(message, f"你这个表情包的id是: {message.sticker.file_id}")
    bot.send_sticker(message.chat.id, 'CAADBQADMQADrGw9CcqcHEC7hwa8Ag')


@bot.message_handler(content_types=['photo'])
def sticker(message):
    print(message)
    bot.reply_to(message, "我日！是图片！我必复读")
    bot.send_message(message.chat.id,  f"想必你就是{message.from_user.first_name}吧。")
    bot.send_photo(message.chat.id, message.photo[0].file_id)

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     # print(message)
#     ret = None
#     try:
#         NSFW_ret = main(message.text)
#         print(NSFW_ret, '\n', message)
#     except Exception as e:
#         ret = f"别试了 我色图库崩了: {e}"
#     print("***")
#     print(message)
#     # photo = open('/tmp/photo.png', 'rb')
#     # bot.send_photo(, photo)
#     # bot.send_photo(chat_id, "FILEID")
#     #
#     if not ret:
#         bot.reply_to(message, ret)

bot.polling()