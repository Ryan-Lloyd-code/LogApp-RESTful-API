from flask_restful import Resource, reqparse
from models.log import LogModel
from models.action import actionModel
from models.properties import propertiesModel
import dateutil.parser

class Log(Resource):
    
    parser = reqparse.RequestParser() 
    parser.add_argument('userId',
                        type=str,
                        required=True,
                        help="Every item needs an action."
                        )     
    
    parser.add_argument('actions',
                        type=dict,
                        required=True,
                        action='append',
                        help="Every item needs an action."
                        )      
    
    def get(self, name):
        log = LogModel.find_by_name(name)
        if log:
            return log.Json()
        return {'message': 'log not found'}, 404

    def post(self, name):
        
        if LogModel.find_by_name(name):
            return {'message': "A log with name '{}' already exists.".format(name)}, 400
        
        data = Log.parser.parse_args()
        log = LogModel(name,data['userId'])

        data=(data['actions'])
        Item=[]
        properties=[]
        for a in range(len(data)):
            Item.append(actionModel(name,dateutil.parser.isoparse(data[a]['date'])))
        for a in range(len(data)):
            properties.append(propertiesModel(name,data[a]['type'],dateutil.parser.isoparse(data[a]['date']),data[a]['properties']))        

        for a in range(len(Item)):
                Item[a].save_to_db()   
                
        for a in range(len(properties)):
                properties[a].save_to_db()                    
        log.save_to_db()


        return log.Json(), 201

    def delete(self, name):
        log = LogModel.find_by_name(name)
        if log:
            log.delete_from_db()

        return {'message': 'log deleted'}


class LogList(Resource):
    def get(self):
        return {'logs': list(map(lambda x: x.Json(), LogModel.query.all()))}
    
class UserId(Resource):
    
    
    def get(self, name):
        log = LogModel.find_by_user(name)
        if log:
            return {'logs': list(map(lambda x: x.Json(), log))}
        return {'message': 'log not found'}, 404
