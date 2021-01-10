from flask import Flask, jsonify
from flask_swagger import swagger

class HomeController():
    def init_app(app):
            @app.route("/")
            def auths():
                swag = swagger(app)
                swag['info']['version'] = "1.0"
                swag['info']['title'] = "My API"
                return jsonify(swag)

            @app.route("/ping")
            def ping():


                return {
                    "result" :
                    {
                        "message" : "失敗",
                        "status" : -1
                    }
                }