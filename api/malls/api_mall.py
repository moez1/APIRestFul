from flask_restful import Resource
from flask import request
from ressources.mall_ressource import MallRessource

class Mall(Resource):
    def get(self,id):
        '''Get mall 
            Input:
                - id: int (id mall)
            Ouput:
                - dict contains a mall
        '''
        mall = MallRessource(id=id,name=None,id_client=None)
        return mall.get_mall()
    
    def put(self,id):
        '''PUT mall 
            Input:
                - id: int (id mall)
            Ouput:
                - dict contains the mall modify
        '''
        some_json = request.get_json()
        mall = MallRessource(id=id,
                            name=some_json['name'] if 'name' in some_json else None,
                            id_client=some_json['id_client'] if 'id_client' in some_json else None)
        return mall.update_mall()
    
    def delete(self,id):
        ''' Delete mall 
            Input:
                - id: int (id mall)
            Ouput:
                - dict contains the mall that was deleted
        '''
        mall = MallRessource(id=id,name=None,id_client=None)
        return mall.delete_mall()
