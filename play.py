import json
import requests

x = """{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""

result = json.loads(x)
print(result)
print(x)
print(result["Name"])
try:
    answers = requests.get(url = 'http://192.168.1.100', verify=False)
except Exception :
    print(f'Exception:{Exception}')
print(answers)


fred='sdgfads'

print(f'hello and {fred} to you')