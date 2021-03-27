from flask import jsonify

from Controllers.BaseController import BaseController

class HomeController(BaseController):
    
    def init_app(self,app,config):
        @app.route('/')
        def HelloWorld():
            return 'Hello World'

        @app.route('/add')
        def add(x,y):
            return x+y

        @app.route('/sub')
        def sub(x,y):
            return x-y

        @app.route('/mult')
        def mult(x,y):
            return x*y

        @app.route('/div')
        def div(x,y):
            return x/y

        @app.route('/mod')
        def mod(x,y):
            return x%y

    
        


    
    
    