"""Generate Members metadata for TheBastionBot GitHub Organization."""

import requests
import json


print('Fetching members info...')

response = requests.get('https://api.github.com/orgs/TheBastionBot/members')
if response.ok:
    print('Generating members metadata...')

    members_info = response.json()
    members = {}

    with open('./data/avatars.json') as avatars:
        avatars = json.load(avatars)

    for member in members_info:
        members[member['login']] = {
            'id': member['id'],
            'avatar': avatars[member['login']] if member['login'] in avatars else ''
        }

    members = json.dumps(members, indent=2)
    members_file = open('./meta/members.json', 'wb')
    members_file.write(str.encode(members))
    members_file.close()

    print('Successfully generated members metadata.')
else:
    response.raise_for_status()
