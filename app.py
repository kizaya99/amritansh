from flask import Flask


class Enrollment_System:
    def __init__(self, name):
        self.app = Flask(name)
        
    
    def setup_route(self):
        @self.app.route('/home')
        def home():
            return '<h1>hehe</h1>'
        def aboutus():
            return '<h1>hoho</h1>'
        
        
    def run(self):
        self.app.run(debug=True)
        
        
x = Enrollment_System(__name__)
x.setup_route()
x.run()
x.happy()
# anythijeinvvvuuchfugnx8xyygcle