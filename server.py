#flask is a module that allows us to write a python service which can send HTTP request
#server.py main module where we imported flask module and created an app using main function we
# can just run app.run, it'll the appl on specific port

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

#We're just going to write a simple hello routine so we can say hello which just returns hi
#and the way we expose HTTP endpoint is by writing app.route

#In our UI application, we want to have a drop down where we want to show all locations & for
# that we're going to write our first routine which will just give us locations so we'll call
#that routine get location names which will return locations.

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#We've created another endpoint predict home price which takes HTTP post method, we have this
#dummy routine which we are going to implement now. The way it works is we have imported this
# requst class & whenever we'll be making HTTP call from our HTML appl we'll get all the inputs
# in request.form
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#What we are doing is we are returning a response which contains all the locations for which we
#are going to create new file called util & util will contain all core routines whereas server
#will just do routing of requests & response.

#We need 2 routines, 1st would be to return the locations in Bglr city, we have our locations in
#column stored in JSON file

if __name__ == "__main__":
    print("Starting Python flask server for Home price prediction...")
    util.load_saved_artifacts()


    app.run()

