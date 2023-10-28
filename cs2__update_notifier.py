import requests
from time import sleep

from utils import read_file, update_file
import telegram_alert


def setup():
    url = 'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=730'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/118.0.0.0 Safari/537.36'
    }
    prev_gid = read_file()

    check_for_updates(url, headers, prev_gid)


def check_for_updates(url, headers, prev_gid):
    while True:
        try:
            response = requests.get(url, headers=headers).json()
            latest_update = response['appnews']['newsitems'][0]
            gid = latest_update['gid']

            if prev_gid is not None:
                if gid != prev_gid:
                    prev_gid = gid
                    update_file(prev_gid)
                    print(f"Found new update: {latest_update['title']}")

                    telegram_alert.send_alert(
                        f"Title: {latest_update['title']}\n"
                        f"Description: \n{latest_update['contents']}\n"
                        f"{latest_update['url']}"
                    )
                    sleep(6000)
                else:
                    print("No new updates")
            else:
                prev_gid = gid
                update_file(prev_gid)

        except Exception as ex:
            print(f"Error happened: {ex}")

        print("Waiting...")
        sleep(600)


if __name__ == "__main__":
    setup()
