import requests
import json
# end_point = 'https://www.delfi.lt/'
#
# data = requests.get('http://127.0.0.1:5000/json/keliamieji/1')
#
#
#
# value = data.json()
#
# value_1 = json.dumps(value)
#
# value_2 = json.loads(data.text)
#
# print(value_1)
# print(type(value_1))
# print(value)
# print(type(value))
# print(data.text)
# print(type(data.text))
# print(value_2)
# print(type(value_2))


# payload = {'vardas': 'Donatas', 'pavarde': 'Noreika', 'amzius': 2000}
# r = requests.post('http://127.0.0.1:5000/json', json=payload)
# dictionary = json.loads(r.text)
# print(dictionary)
#
# # {'you sent': {'amzius': 2000, 'pavarde': 'Noreika', 'vardas': 'Donatas'}}
#
# r2 = requests.get('http://127.0.0.1:5000/json/keliamieji/2100')
# dictionary2 = json.loads(r2.text)
# print(dictionary2['result'])

req = requests.get('http://127.0.0.1:5000/api/books/1')
# data = req.json()
# print(req)
