from db import db


class LogModel(db.Model):
    __tablename__ = 'logs'
#creating logs table
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(80))
    userId = db.Column(db.String(80))

    items = db.relationship('actionModel', lazy='dynamic')

    def __init__(self, sessionId, userId):
        self.sessionId = sessionId
        self.userId = userId

    def Json(self):
        return {'userId':self.userId,'sessionId':self.sessionId,'actions': [item.Json() for item in self.items.all()]}
    
#finds a log via the sessionId     
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(sessionId=name).first()
    
#finds a all logs belonging to a user     
    @classmethod
    def find_by_user(cls, userId):
        return cls.query.filter_by(userId=userId).all()    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
