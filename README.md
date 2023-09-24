# CS Update Notifier
This program notifies you when a new CS Update released.

REQUIREMENTS
------------
1. __Feedparser:__ This library is used to parse the RSS feed from the official CS blog and retrieve information about updates. For installation details, visit the [PyPI page](https://pypi.org/project/feedparser/). 
2. __BeautifulSoup4:__ BeautifulSoup4 is used to format the obtained text to make it more readable for notifications. For installation details, visit the [PyPI page](https://pypi.org/project/beautifulsoup4/).
3. __Telegram Python Library:__ This library allows you to send notifications via Telegram. For installation details, visit the [PyPI page](https://pypi.org/project/pyTelegramBotAPI/).

INFO
------------
This program doesn't use your login details it's just parse CS RSS-feed for the new updates every 10 minutes.
