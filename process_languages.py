# encoding=utf8
import os
import json


all_languages = {}
language_count = {}
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.languages'):
            continue
        with open(os.path.join(root, f)) as fp:
            languages = json.loads(fp.read())

        languages_curated = set()
        for language in languages.get('languages', []):
            if language['name'] in ('Spanish', 'Espanhol', 'Espa\u00f1ol'):
                languages_curated.add(u'Español')
            elif language['name'] in (u'Inglés',):
                languages_curated.add(u'English')
            elif language['name'] in (u'Francés', 'French', 'France'):
                languages_curated.add(u'Français')
            elif language['name'] in (u'Italian',):
                languages_curated.add(u'Italiano')
            elif language['name'] in (u'German', u'Alemán', 'Aleman'):
                languages_curated.add(u'Deutsch')
            elif language['name'] in (u'Hebreo',):
                languages_curated.add(u'Hebrew')
            elif language['name'] in (u'Portuguese',):
                languages_curated.add(u'Português')
            else:
                languages_curated.add(language['name'])

        for language in languages_curated:
            if language not in all_languages:
                all_languages[language] = language

            if language not in language_count:
                language_count[language] = 1
            else:
                language_count[language] += 1

flares = []
for language in all_languages.values():
    flares.append({'name': language, 'size': language_count[language]})
print json.dumps({'name': 'Flare', 'children': flares}, indent=2)
