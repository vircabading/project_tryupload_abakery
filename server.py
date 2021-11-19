from flask_app import app                                               # Import flask app
from flask_app.controllers import root_controller                      # Import Controllers
from flask_app.controllers import cake_controller

if __name__=="__main__":   
    app.run(debug=True)    