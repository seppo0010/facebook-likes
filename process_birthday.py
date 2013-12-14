# encoding=utf8
import os
import json


all_birthdays = {}
birthday_count = {}
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.birthday'):
            continue
        with open(os.path.join(root, f)) as fp:
            data = json.loads(fp.read())

        if 'birthday' not in data:
            continue

        birthday = data['birthday'][:5]
        if birthday not in all_birthdays:
            all_birthdays[birthday] = birthday

        if birthday not in birthday_count:
            birthday_count[birthday] = 1
        else:
            birthday_count[birthday] += 1

flares = []
for birthday in all_birthdays.values():
    flares.append({'name': birthday, 'size': birthday_count[birthday]})
print json.dumps({'name': 'Flare', 'children': flares}, indent=2)
