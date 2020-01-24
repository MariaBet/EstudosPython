

import json

d1 = {
    'Pessoa1': {
        'nome': 'Maria',
        'idade': 28,
    },
    'Pessoa2': {
        'nome': "Honorio",
        'idade': 29,
    },
}
d1_json = json.dumps(d1,indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
