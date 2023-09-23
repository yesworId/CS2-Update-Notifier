import telebot


def send_alert(message):
    bot = telebot.TeleBot('YOUR_BOT_TOKEN')
    chat_id = 'YOUR_CHAT_ID_TOKEN'
    bot.send_message(chat_id, text=message, parse_mode='Markdown')
