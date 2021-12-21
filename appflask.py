from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello Digeiz!</p>"

from api.clients.api_clients import Clients
from api.clients.api_client import Client

from api.malls.api_malls import Malls
from api.malls.api_mall import Mall

from api.unites.api_unites import Unites
from api.unites.api_unite import Unite

api.add_resource(Clients, "/clients/"),
api.add_resource(Client, "/client/<id>/"),

api.add_resource(Malls, "/malls/"),
api.add_resource(Mall, "/mall/<int:id>/"),

api.add_resource(Unites, "/unites/"),
api.add_resource(Unite, "/unite/<int:id>/"),

app.run(port=5000)