from flask import Flask, render_template


class Enrollment_System:
    def __init__(self, name):
        self.app = Flask(name)
        
    
    def setup_route(self):
        @self.app.route('/home')
        def home():
            return render_template("home.html")
        def aboutus():
            return '<h1>hoho</h1>'
        
        
    def run(self):
        self.app.run(debug=True)
        
        
x = Enrollment_System(__name__)
x.setup_route()
x.run()
