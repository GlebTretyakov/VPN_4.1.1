def create_user_in_config():
    file = open('test_config.json', 'a')
    file.write()
    file.close()

create_user_in_config()


import uuid
import json

str(uuid.uuid4())
begin = '\n\n          {'
end = '\n          },'
tab = '\n            '
id = '"id": "2544c179-ea31-4800-929f-64b6ecb36527",'
tg_id = '"tg-id": "kent-Z.D.D-2-ok",'
flow = '"flow": "xtls-rprx-vision"'

print(tg_id)
print(flow)

def create_user_in_config():
    file = open('test_config.json', 'a')
    file.write('')
    file.close()



with open('config.json') as f:
    myNames = f.readlines()

print(myNames)



with open('config.json') as f:
    data = json.load(f)
    print(data)

with open('data.json', 'w') as f:
    json.dump(data, f)