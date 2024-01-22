from flask import Flask
from flask import request
from flask import jsonify
import requests


app = Flask(__name__)



import uuid
import json


config_begin = '{"log": {"loglevel": "info"},"routing": {"rules": [],"domainStrategy": "AsIs"},"inbounds": [{"port": 2011,"tag": "ss","protocol": "shadowsocks","settings": {"method": "2022-blake3-aes-128-gcm","password": "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb","network": "tcp,udp"}},{"port": 143,"protocol": "vless","tag": "vless_tls","settings": {"clients":[\n'
config_end = '\n\n{"id": "2544c179-ea31-4800-929f-64b6ecb36527", "tg-id": "kent-Z.D.D-2-ok", "flow": "xtls-rprx-vision"}],"decryption": "none", "fallbacks": [{"path": "/myverysecretpath", "dest": "@vless-ws"}, {"dest": "8080"}]}, "streamSettings": {"network": "tcp", "security": "tls", "tlsSettings": {"alpn": ["http/1.1", "h2"], "certificates": [{"certificateFile": "/etc/letsencrypt/live/vpn-test.ru/fullchain.pem", "keyFile": "/etc/letsencrypt/live/vpn-test.ru/privkey.pem"}]}}, "sniffing": {"enabled": true, "destOverride": ["http", "tls"]}}, {"listen": "@vless-ws", "protocol": "vless", "tag": "vless_ws", "settings": {"clients": [{"id": "7957c33c-d9ca-11ed-afa1-0242ac120002", "email": "user2@myserver"}], "decryption": "none"}, "streamSettings": {"network": "ws", "security": "none", "wsSettings": {"path": "/myverysecretpath"}}}], "outbounds": [{"protocol": "freedom", "tag": "direct"}, {"protocol": "blackhole", "tag": "block"}]}'

str(uuid.uuid4())
begin = '\n\n{'
end = '\n},'
tab = '\n'
id = '\n"id": "2544c179-ea31-4800-929f-64b6ecb36527",'
tg_id = '\n"tg-id": "kent-Z.D.D-2-ok",'
flow = '\n"flow": "xtls-rprx-vision"'


def create_user_in_config():
    file = open('test_config.json', 'a')
    file.write(config_begin)
    file.write(begin + id + tg_id + flow + end)
    file.write(begin + id + tg_id + flow + end)
    file.write(begin + id + tg_id + flow + end)
    file.write(config_end)
    file.close()

config_user = '{"id": "2544c179-ea31-4800-929f-64b6ecb36527","tg-id": "kent-Z.D.D-2-ok","flow": "xtls-rprx-vision"}'

json_config_user = json.loads(config_user)

#print(json_config_user)


#res = requests.post('https://9390-62-217-190-86.ngrok-free.app/test_create_config', data='{"id": "test","tg-id": "test_1": "xtls-rprx-vision"}')
#print(res.text)

@app.route('/test_create_config', methods=['POST'])
def add_message():
    config_data = request
    user_uuid = config_data.json["id"]
    user_id = config_data.json["tg-id"]
    protocol = config_data.json["flow"]
    print(user_uuid + '\'n' + '\n' + user_id + '\n' + protocol)

    return json.dumps(json_config_user), 200


if __name__ == '__main__':
    app.run()



#print(tg_id)
#print(flow)




#print(config_data.get_json(force=True))
#json_response_CREATE_CONFIG_FAIL = {"Config_created": "FAIL"}
#print('JSON ' + json.dumps(json_config_user))