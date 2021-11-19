from flask_app import app                                               # App is used to handle routes
from flask import render_template, session, redirect, request, jsonify
from flask_app.models import cakes_model                                # Import the cakes model in order to use Cakes

# ////////////////////////////////////////////////////////
# ROOT CONTROLLER
# ////////////////////////////////////////////////////////

# //// SHOW /////////////////////////////////////

@app.route('/')                                                         # Main Page
def root():
    print("@@@@ Root @@@@")
    all_cakes = cakes_model.Cakes.get_all()                             # Get All instances of Cakes in the Cakes DB
    print("Retrieving all cakes")
    print("Retrieved", len(all_cakes), "cakes")
    return render_template("index.html", all_cakes = all_cakes)

# //// UTILITIES /////////////////////////////////

# //// CREATE ////////////////////////////////////


# //// RETRIEVE ////////////////////////////////////


# //// UPDATE ////////////////////////////////////


# //// DELETE ////////////////////////////////////


# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."