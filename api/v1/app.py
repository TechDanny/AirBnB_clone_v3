#!/usr/bin/python3
""" app """


from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage


app = Flask(__name__) 
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ teardown func """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """ returns 404 json error """
    data = {
            "error": "Not found"
            }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
