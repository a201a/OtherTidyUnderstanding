import os
import telebot

# الحصول على التوكن من متغيرات البيئة
TOKEN = '7451602082:AAGc7goOfmBrWbGG3R8PJLZBPToR_unI8OQ'

# إنشاء كائن البوت
bot = telebot.TeleBot(TOKEN)

# تعريف دالة الاستجابة للأمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! This is your bot.")

# تشغيل البوت
if __name__ == "__main__":
    bot.polling()