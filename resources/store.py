import re
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if name:
            return store.json()
        return {'message': 'store not found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "store with name {} already exists".format(name)}, 404
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'error has occured'}, 500
        
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'store delete'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
