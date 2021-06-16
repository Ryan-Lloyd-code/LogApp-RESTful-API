from flask_restful import Resource, reqparse
from models.action import actionModel
from models.log import LogModel
from models.properties import propertiesModel

import dateutil.parser


#finding logs within a certain date range
#This function takes in two date arguments. It should then return all logs that have occured between and including those dates
class Date(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('start_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    
    parser.add_argument('end_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    
    def get(self):
        date = Date.parser.parse_args()
        date_start = dateutil.parser.isoparse(date['start_date'])
        date_end = dateutil.parser.isoparse(date['end_date'])
        actions = actionModel.find_by_date(date_start,date_end)
        logs =[]
        for i in range(len(actions)):
            logs.append(LogModel.find_by_name(actions[i].sessionId))
        logs = list(set(logs))

        if actions:         
            return {'logs': list(map(lambda x: x.Json(), logs))}
        return {'message': 'Item not found'}, 404

#Finding logs bt TYPE of request
#This function returns all logs in which the desired TYPE of action occured
class Type(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('type',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
        
    def get(self,name):
        
        props = propertiesModel.find_by_type(name)
        logs =[]

        for i in range(len(props)):
            logs.append(LogModel.find_by_name(props[i].sessionId))
        logs = list(set(logs))

        if props:         
            return {'logs': list(map(lambda x: x.Json(), logs))}
        return {'message': 'Item not found'}, 404

