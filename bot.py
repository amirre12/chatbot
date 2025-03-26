import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # دریافت توکن از متغیر محیطی

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! 👋 این یک ربات تستی است که روی Railway اجرا شده است.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("ربات در حال اجرا است...")
bot.infinity_polling()
