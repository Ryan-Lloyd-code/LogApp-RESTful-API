from db import db
#import json

class actionModel(db.Model):
    __tablename__ = 'actions'
#creating actions table
    id = db.Column(db.Integer, primary_key=True)
#links to logs table via sessionId
    sessionId = db.Column(db.Integer, db.ForeignKey('logs.sessionId'))
    date = db.Column(db.DateTime(timezone=True))
    
    store = db.relationship('LogModel')
    props = db.relationship('propertiesModel', uselist = False)

    def __init__(self, sessionId,date):

        self.sessionId = sessionId
        self.date = date
        
    def Json(self):
        return {'time': self.date.__str__(), 'type':self.props.Type, 'properties': self.props.Json()}
    
#find logs that occured within a date range    
    @classmethod
    def find_by_date(cls, start_date,end_date):
        return cls.query.filter(actionModel.date >= start_date).filter(actionModel.date <= end_date).all()    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
