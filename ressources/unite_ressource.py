''' This file contains the UniteResource class in which I GET, POST, PUT and DELETE Unite'''


from core.pagination import Pagination
from flask import request,jsonify

unites = [
    {'id':5,'name':'unite1','id_mall':9},
    {'id':6,'name':'unite2','id_mall':10},
    {'id':7,'name':'unite3','id_mall':11}
]


class UniteRessource:
    '''
    this class contains the different GET POST PUT and DELETE operations for Unites
    '''

    def __init__(self, id:int, name:str, id_mall:int):
        '''
        unite class constructor
        Input:
            - id: int (id of unite)
            - name: str (name of unite)
            - id_client: int (id of mall)
        '''
        self.id = id
        self.name = name
        self.id_mall = id_mall
    
    def get_all_unites(self):
        '''
        GET ALL unites
        Output:
            - list of dict contains all unites
        '''
        return jsonify(Pagination.get_paginated_list(
        unites,
        '/unites/',
        start = request.args.get('start', 1),
        limit = request.args.get('limit', 2)
        ),200)
    
    def get_unite(self):
        '''
        GET unite
        Output:
            - dict of unite 
        '''
        res = [x for x in unites if x['id'] == self.id]
        return (res[0],200) if res else ({'details':'verify les inputs'},400)

    
    def insert_unite(self):
        '''
        POST unite
        Output:
            - unite dict inserted
        '''
        try:
            unites.append(self.__dict__)
            return self.__dict__,201
        except:
            return {'details':'verify les inputs'},400

    def update_unite(self):
        '''
        PUT unite
        Output:
            - unite dict updated
        '''
        res={'detail':'error'},400
        for line in unites:
            if self.id == line['id']:
                line['name']=self.name if self.name else line['name']
                line['id_mall']=self.id_mall if self.id_mall else line['id_mall']
                res = line,201
        return res

    def delete_unite(self):
        '''
        DELETE unite
        Output:
            - unite dict deleted
        '''
        res={'detail':'error'},400
        elem = [x for x in unites if x['id'] == self.id]
        if elem:
            unites.remove(elem[0])        
            res = elem[0],200
        return res