# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:26:32 2021

@author: gilli
"""

from db import db
#import json



class propertiesModel(db.Model):
    __tablename__ = 'properties'
#creating properties table
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(80))
#links to logs table via the sessionId
    sessionId = db.Column(db.Integer, db.ForeignKey('logs.sessionId'))
    locationX = db.Column(db.Integer)
    locationY = db.Column(db.Integer)
    viewedId = db.Column(db.String(80))
    pageFrom = db.Column(db.String(80))
    pageTo = db.Column(db.String(80))
    date = db.Column(db.DateTime(timezone=True),db.ForeignKey('actions.date') )

    
    def __init__(self, sessionId, Type, date, props):
        
        if Type == 'CLICK':           
            self.Type = Type
            self.sessionId = sessionId
            self.locationX = props['locationX']
            self.locationY = props['locationY']
            self.date = date

        if Type == 'VIEW':           
            self.Type = Type
            self.sessionId = sessionId
            self.viewedId = props['viewedId']
            self.date = date
            
        if Type == 'NAVIGATE':           
            self.Type = Type
            self.sessionId = sessionId
            self.pageFrom = props['pageFrom'] 
            self.pageTo = props['pageTo']
            self.date = date
            
        
    def Json(self):
        if self.Type == 'CLICK':
            return {'locationX': self.locationX, 'locationY':self.locationY}
        elif self.Type == 'VIEW':
            return {'viewedId': self.viewedId}
        elif self.Type == 'NAVIGATE':
            return {'pageFrom':self.pageFrom, 'pageTo':self.pageTo}

    @classmethod
#Find logs that have the desired Type of action
    def find_by_type(cls, Type):
        return cls.query.filter_by(Type=Type).all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

        