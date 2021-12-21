from flask_restful import Resource
from flask import request
from ressources.client_ressource import ClientRessource

class Clients(Resource):
    def get(self):
        '''
        GET all clients
        Output:
            - list of dict contains all clients
        '''
        client = ClientRessource(id=None,name=None)
        return client.get_all_clients()
    
    def post(self):
        '''
        Post client
        Output:
            - client dict inserted
        '''
        some_json = request.get_json()
        client = ClientRessource(id=some_json['id'],name=some_json['name'])
        return client.insert_client()
