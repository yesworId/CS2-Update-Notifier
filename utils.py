import os
import json


def read_file():
    if os.path.exists('cache.json'):
        with open('cache.json') as cache_file:
            gid = json.load(cache_file)['gid']
        return gid
    else:
        create_file()
        return None


def create_file():
    gid = {'gid': None}
    with open('cache.json', 'w') as file:
        json.dump(gid, file)
    print("Created cache.json file")


def update_file(new_gid):
    gid = {'gid': new_gid}
    with open('cache.json', 'w') as file:
        json.dump(gid, file)
