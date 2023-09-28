import os
import json
import feedparser
from time import sleep

import telegram_alert


def setup():
    url = 'https://steamcommunity.com/games/CSGO/rss'
    latest_date = get_date()
    check_for_updates(url, latest_date)


def get_date():
    if os.path.exists('date.json'):
        latest_date = json.load(open('date.json'))['latest_update_date']
        return latest_date
    else:
        create_date_file()
        return None


def check_for_updates(url, latest_date):
    while True:
        try:
            feed = feedparser.parse(url)
            latest_entry = feed.entries[0]
            entry_date = feed.entries[0].published

            if latest_date is not None:
                if entry_date != latest_date:
                    latest_date = entry_date
                    update_date(latest_date)
                    print(f"Found a new update: {latest_entry.title}")
                    telegram_alert.send_alert()
                else:
                    print("There is no new update")
            else:
                latest_date = entry_date
                update_date(latest_date)
                print("Saved latest update date")

        except Exception as ex:
            print(f"Error happened: {ex}")
        print("Waiting...")
        sleep(600)


def create_date_file():
    date = {'latest_update_date': None}
    with open('date.json', 'w') as file:
        json.dump(date, file)
    print("Created date.json file")


def update_date(new_date):
    date = {'latest_update_date': new_date}
    with open('date.json', 'w') as file:
        json.dump(date, file)


if __name__ == "__main__":
    setup()
