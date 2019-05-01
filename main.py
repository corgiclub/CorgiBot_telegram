import telebot
from config import TOKEN
from pixivBot.main import main
bot = telebot.TeleBot(TOKEN)

print(bot.get_me())
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

#
# @bot.message_handler(regexp="来.*色图")
# def handle_message(message):
#     print(message)
#     bot.reply_to(message, "狗东西看你妈呢")

@bot.message_handler(content_types=['sticker'])
def sticker(message):
    print(message)
    bot.reply_to(message, f"想必你就是{message.from_user.first_name}吧。我日！是表情包！")
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
#
bot.polling()