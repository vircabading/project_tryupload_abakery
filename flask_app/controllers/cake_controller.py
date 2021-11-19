from flask_app import app                                               # App is used to handle routes
from flask import render_template, session, redirect, request, jsonify
from flask_app.models import cakes_model                                # Import the cakes model in order to use Cakes

# ////////////////////////////////////////////////////////
# ROOT CONTROLLER
# ////////////////////////////////////////////////////////

# //// SHOW /////////////////////////////////////



# //// POST //////////////////////////////////////

@app.route('/cakes/search/post', methods = ['POST'])
def cakes_search_post():
    print("@@@@ In Cakes Search POST @@@@")
    session['searchitem']= request.form['search-item']
    print("Session search item", session['searchitem'])
    return redirect ("/cakes/search")

# //// UTILITIES /////////////////////////////////

# //// CREATE ////////////////////////////////////


# //// RETRIEVE //////////////////////////////////

@app.route('/cakes/christening')                            # //// GET ALL CHRISTENING CAKES ////////
def cakes_christening():
    print("@@@@ Cakes / Christening @@@@")
    data = {
        'category': "christening"
    }
    all_cakes = cakes_model.Cakes.get_all_by_category(data)
    return render_template("cakes_christening.html", all_cakes = all_cakes)

@app.route('/cakes/debut')                                  # //// GET ALL DEBUT CAKES ////////
def cakes_debut():
    print("@@@@ Cakes / Debut @@@@")
    data = {
        'category': "debut"
    }
    all_cakes = cakes_model.Cakes.get_all_by_category(data)
    return render_template("cakes_debut.html", all_cakes = all_cakes)

@app.route('/cakes/wedding')                                # //// GET ALL WEDDING CAKES ////////
def cakes_wedding():
    print("@@@@ Cakes / Wedding @@@@")
    data = {
        'category': "wedding"
    }
    all_cakes = cakes_model.Cakes.get_all_by_category(data)
    return render_template("cakes_wedding.html", all_cakes = all_cakes)

@app.route('/cakes/birthday')                                # //// GET ALL WEDDING CAKES ////////
def cakes_birthday():
    print("@@@@ Cakes / Birthday @@@@")
    data = {
        'category': "birthday"
    }
    all_cakes = cakes_model.Cakes.get_all_by_category(data)
    return render_template("cakes_birthday.html", all_cakes = all_cakes)

@app.route('/cakes/search')
def cakes_search():
    print("@@@@ Cakes Search @@@@")
    data = {
        'searchitem': "%" + session['searchitem'] + "%"
    }
    print("Data:", data)
    all_cakes = cakes_model.Cakes.get_all_by_search_item(data)
    return render_template("cakes_search.html", all_cakes = all_cakes)

# //// UPDATE ////////////////////////////////////


# //// DELETE ////////////////////////////////////


# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."