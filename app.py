from flask import Flask                                                                                                                                        
from Controllers import HomeController
app = Flask(__name__ )
Config = ''
HomeController.HomeController().init_app(app,Config)