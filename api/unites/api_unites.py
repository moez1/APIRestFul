from flask_restful import Resource
from flask import request
from ressources.unite_ressource import UniteRessource

class Unites(Resource):
    def get(self):
        '''
        GET all unites
        Output:
            - list of dict contains all unites
        '''
        unite = UniteRessource(id=None,name=None,id_mall=None)
        return unite.get_all_unites()
    
    def post(self):
        '''
        Post unite
        Output:
            - unite dict inserted
        '''
        some_json = request.get_json()
        unite = UniteRessource(id=some_json['id'],
                             name=some_json['name'],
                             id_mall=some_json['id_mall'])
        return unite.insert_unite()
