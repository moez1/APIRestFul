''' This file contains the MallResource class in which I GET, POST, PUT and DELETE Mall'''

from core.pagination import Pagination
from flask import request,jsonify

malls = [
    {'id':5,'name':'mall1','id_client':9},
    {'id':6,'name':'mall2','id_client':10},
    {'id':7,'name':'mall3','id_client':11}
]


class MallRessource:
    '''
    this class contains the different GET POST PUT and DELETE operations for Malls
    '''

    def __init__(self, id:int, name:str, id_client:int):
        '''
        client class constructor
        Input:
            - id: int (id of mall)
            - name: str (name of mall)
            - id_client: int (id of client)
        '''
        self.id = id
        self.name = name
        self.id_client = id_client
    
    def get_all_malls(self):
        '''
        GET ALL malls
        Output:
            - list of dict contains all malls
        '''
        return jsonify(Pagination.get_paginated_list(
        malls,
        '/malls/',
        start = request.args.get('start', 1),
        limit = request.args.get('limit', 2)
        ),200)
    
    def get_mall(self):
        '''
        GET mall
        Output:
            - dict of mall 
        '''
        res = [x for x in malls if x['id'] == self.id]
        print (res[0] if res else {'details':'verify les inputs'},400)
        return res[0],200 if res else ({'details':'verify les inputs'},400)

    
    def insert_mall(self):
        '''
        POST mall
        Output:
            - mall dict inserted
        '''
        try:
            malls.append(self.__dict__)
            return self.__dict__,201
        except:
            return {'details':'verify les inputs'},400

    def update_mall(self):
        '''
        PUT mall
        Output:
            - mall dict updated
        '''
        res={'detail':'error'},400
        for line in malls:
            if self.id == line['id']:
                line['name']=self.name if self.name else line['name']
                line['id_client']=self.id_client if self.id_client else line['id_client']
                res = line,201
        return res

    def delete_mall(self):
        '''
        DELETE mall
        Output:
            - mall dict deleted
        '''
        res={'detail':'error'},400
        elem = [x for x in malls if x['id'] == self.id]
        if elem:
            malls.remove(elem[0])        
            res = elem[0],204
        return res