from flask import jsonify
import requests
import json
from flask import request
class TelegramController():
    def init_app(app):
            @app.route("/telegram/tgyuhaobot", methods=['POST'])
            def tgyuhaobot():

                text = request.get_json()['text']
                api = f"https://api.telegram.org/bot1585024002:AAGx_sWgIB8IB90GQhgNQIvzfc5patQ6JtY/sendMessage?chat_id=922219145&text={text}"
                res = requests.get(api)
                result = json.loads(res.text)
                return result