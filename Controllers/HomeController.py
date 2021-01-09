class HomeController():
    def init_app(app):
            @app.route("/")
            def auths():
                return {"nmae":"Tony1"}

            @app.route("/ping")
            def ping():

               
                return { 
                    "result" :  
                    {
                        "message" : "失敗", 
                        "status" : -1
                    }
                }