import logging
from aiogram import Bot, Dispatcher
from flask import Flask
from flask import request
from flask import jsonify
import asyncio
import json
import uuid
from yookassa import Configuration, Payment

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

token2 = '5871751859:AAHR3Qdf6QktLnbB0wczWFaLQn3Hxf28BHo'
bot = Bot(token=token2)
#dp = Dispatcher(bot)

chat_id_my = 938346742


async def send_message(chat_id, text):
    await bot.send_message(str(chat_id), text)


def check_if_successful_payment(request):
    try:
        if request.json["event"] == "payment.succeeded":
            return jsonify(f'PAY:OK')
    except KeyError:
        return False

    return False


@app.route('/yookassa_test', methods=['GET'])


@app.route('/yookassa_test', methods=['POST'])
def yookassa_pay():
    try:
        yookassa_response = jsonify(request.json)
        if yookassa_response.json["event"] == "payment.succeeded":
            asyncio.run(send_message(chat_id_my, "Payment successful"))
            json_response_PAY_OK = {"payment": "successful"}
            return json.dumps(json_response_PAY_OK), 200
        else:
            json_response_PAY_FAIL = {"payment": "FAIL"}
            return json_response_PAY_FAIL, 200
    except KeyError:
        json_response_PAY_FAIL = {"payment": "FAIL"}
        return json.dumps(json_response_PAY_FAIL), 200


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)


#async def on_startup(x):
    #asyncio.create_task(asyncio.to_thread(app.run))

#if __name__ == '__main__':
    #executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
