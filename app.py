from flask import Flask

from Controllers import HomeController
from Controllers import TelegramController

app=Flask(__name__)

HomeController.HomeController.init_app(app)
TelegramController.TelegramController.init_app(app)

if __name__ =="__main__":
    app.run()