import telebot


def send_alert():
    bot = telebot.TeleBot('YOUR_BOT_TOKEN')
    chat_id = 'YOUR_CHAT_ID_TOKEN'
    bot.send_message(chat_id, text=f"WAKE UP! New CS Update Released!", parse_mode='Markdown')
