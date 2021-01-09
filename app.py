from flask import Flask

from Controllers import HomeController

app=Flask(__name__)

HomeController.HomeController.init_app(app)

if __name__ =="__main__":
    app.run()