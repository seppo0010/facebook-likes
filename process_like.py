import os
import json


all_likes = {}
like_count = {}
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.likes'):
            continue
        with open(os.path.join(root, f)) as fp:
            likes = json.loads(fp.read())
        for like in likes['data']:
            if like['id'] not in all_likes:
                all_likes[like['id']] = like

            if like['id'] not in like_count:
                like_count[like['id']] = 1
            else:
                like_count[like['id']] += 1

flares = {}
for like in all_likes.values():
    if like['category'] not in flares:
        flares[like['category']] = {'name': like['category'], 'children': []}
    flares[like['category']]['children'].append({'name': like['name'], 'size': like_count[like['id']]})
print json.dumps({'name': 'Flare', 'children': flares.values()}, indent=2)
