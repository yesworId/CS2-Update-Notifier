# CS Update Notifier
This program notifies you when a new CS Update released.

## REQUIREMENTS
1. __Requests:__ Requests allows you to send HTTP/1.1 requests extremely easily. [PyPI page](https://pypi.org/project/requests/). 
2. __Telegram Python Library:__ This library allows you to send notifications via Telegram. For installation details, visit the. [PyPI page](https://pypi.org/project/pyTelegramBotAPI/).

## INFO
This program was made to notify about new CS2 update. 

It just parses CS2 Blog page every 10 minutes and compares id of the new update with previous one, which is saved in cache.json file. After It detected new update, bot sends alert message.

You can use your own methods for the notification. To get Telegram alert working, you will need to create a Telegram bot in BotFather and obtain bot token with your ChatID. Then change this parameters in telegram_alerts.py
