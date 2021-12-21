''' This file contains the ClientResource class in which I GET, POST, PUT and DELETE Client'''
from flask import request,jsonify
from core.pagination import Pagination

clients = [
    {'id':5,'name':'client1'},
    {'id':6,'name':'client2'},
    {'id':7,'name':'cleint3'}
]

class ClientRessource():
    '''
    this class contains the different GET POST PUT and DELETE operations for Clients
    '''
    def __init__(self, id:int, name:str):
        '''
        client class constructor
        Input:
            - id: int (id of client)
            - name: str (name of client)
        '''
        self.id = id
        self.name = name
    
    def get_all_clients(self):
        '''
        GET ALL Clients
        Output:
            - list of dict contains all clients
        '''
        return jsonify(Pagination.get_paginated_list(
        clients,
        '/clients/',
        start = request.args.get('start', 1),
        limit = request.args.get('limit', 2)
        ),200)
    
    def get_client(self):
        '''
        GET client
        Output:
            - dict of client 
        '''
        res = [x for x in clients if x['id'] == self.id]
        return res[0],200 if res else ({'details':'verify les inputs'},400)

    
    def insert_client(self):
        '''
        POST client
        Output:
            - client dict inserted
        '''
        try:
            clients.append(self.__dict__)
            return self.__dict__,201
        except:
            return {'details':'verify les inputs'},400

    def update_client(self):
        '''
        PUT client
        Output:
            - client dict updated
        '''
        res={'detail':'error'},400
        for line in clients:
            if self.id == line['id']:
                line['name']=self.name if self.name else line['name']
                res = line,201
        return res

    def delete_client(self):
        '''
        DELETE client
        Output:
            - client dict deleted
        '''
        res={'detail':'error'},400
        elem = [x for x in clients if x['id'] == self.id]
        if elem:
            clients.remove(elem[0])        
            res = elem[0],204
        return res