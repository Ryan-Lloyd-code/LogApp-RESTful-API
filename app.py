from flask import Flask
from flask_restful import Api

from resources.action import Date, Type
from resources.log import Log, LogList, UserId

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

#adds log
api.add_resource(Log, '/log')
#returns all logs
api.add_resource(LogList, '/logs')
#returns logs within a date range
api.add_resource(Date, '/date')
#returns logs that have an action of the desired type
api.add_resource(Type, '/type/<string:name>')
#returns logs belonging to userId
api.add_resource(UserId,'/id/<string:name>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True, use_reloader=False) 
