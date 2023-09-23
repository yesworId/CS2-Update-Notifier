import telebot


def send_alert(message):
    bot = telebot.TeleBot('YOUR_BOT_TOKEN')
    chat_id = 'YOUR_CHAT_ID_TOKEN'
    bot.send_message(chat_id, text=f"WAKE UP! New CS Update Released! \n\n{message}", parse_mode='Markdown')
