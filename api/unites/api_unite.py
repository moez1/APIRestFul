from flask_restful import Resource
from flask import request
from ressources.unite_ressource import UniteRessource

class Unite(Resource):
    def get(self,id):
        '''Get unite 
            Input:
                - id: int (id unite)
            Ouput:
                - dict contains a unite
        '''
        unite = UniteRessource(id=id,name=None,id_mall=None)
        return unite.get_unite()
    
    def put(self,id):
        '''PUT mall 
            Input:
                - id: int (id unite)
            Ouput:
                - dict contains the unite modify
        '''
        some_json = request.get_json()
        unite = UniteRessource(id=id,
                            name=some_json['name'] if 'name' in some_json else None,
                            id_mall=some_json['id_mall'] if 'id_mall' in some_json else None)
        return unite.update_unite()
    
    def delete(self,id):
        ''' Delete unite 
            Input:
                - id: int (id unite)
            Ouput:
                - dict contains the unite that was deleted
        '''
        unite = UniteRessource(id=id,name=None,id_client=None)
        return unite.delete_unite()
