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


def format_text(text: str) -> str:
    lines = text.split('\n')
    formatted_lines = []
    indent = 0

    for line in lines:
        if '[list]' in line:
            indent += 1
            continue
        elif '[/list]' in line:
            indent -= 1
            continue

        indentation = '    ' * indent
        marker = '•' if '[*]' in line else ''
        formatted_line = f"{indentation}{marker} {line.replace('[*] ', '').strip()}"
        formatted_lines.append(formatted_line)

    formatted_text = '\n'.join(formatted_lines)
    return formatted_text
