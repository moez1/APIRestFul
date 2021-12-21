from flask_restful import Resource
from flask import request
from ressources.mall_ressource import MallRessource

class Malls(Resource):
    def get(self):
        '''
        GET all malls
        Output:
            - list of dict contains all malls
        '''
        mall = MallRessource(id=None,name=None,id_client=None)
        return mall.get_all_malls()
    
    def post(self):
        '''
        Post mall
        Output:
            - mall dict inserted
        '''
        some_json = request.get_json()
        mall = MallRessource(id=some_json['id'],
                             name=some_json['name'],
                             id_client=some_json['id_client'])
        return mall.insert_mall()
