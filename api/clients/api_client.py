from flask_restful import Resource
from flask import request, jsonify
from ressources.client_ressource import ClientRessource

class Client(Resource):
    def get(self,id):
        '''Get client 
            Input:
                - id: int (id client)
            Ouput:
                - dict contains a client
        '''
        client = ClientRessource(id=id,name=None)
        return client.get_client()
    
    def put(self,id):
        '''PUT client 
            Input:
                - id: int (id client)
            Ouput:
                - dict contains the client modify
        '''
        some_json = request.get_json()
        client = ClientRessource(id=id,name=some_json['name'])
        return client.update_client()
    
    def delete(self,id):
        ''' Delete client 
            Input:
                - id: int (id client)
            Ouput:
                - dict contains the client that was deleted
        '''
        client = ClientRessource(id=id,name=None)
        return client.delete_client()
