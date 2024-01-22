import requests

r = requests.post('https://aa83-2a03-d000-4326-cd62-287d-d929-cbdc-5f3c.ngrok-free.app/test_create_config', json={"id": "324324", "tg-id": "test_1", "flow": "xtls-rprx-vision"})
print(r.json())