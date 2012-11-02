#!/usr/bin/env python
# coding=utf8

from flask import Blueprint
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Block(db.Model):
    __tablename__ = 'contentblocks_block'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    type = db.Column(db.String(120), unique=True)

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return "<Block('%s')>" % (self.name)

class Content(db.Model):
    __tablename__ = 'contentblocks_content'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    block_id = db.Column(db.Integer, db.ForeignKey('contentblocks_block.id'))

    def __init__(self, content, block):
        self.content = content
        self.block_id = block

    def __repr__(self):
        return "<Block('%s')>" % (self.content)

class ContentBlocks(object):
    def __init__(self, app=None):
        self.app = None
        
        if app is not None:
            self.app = app
            self.init_app(self.app)
    
    def init_app(self, app):
        blueprint = Blueprint(
            'ContentBlocks',
            __name__)

        app.register_blueprint(blueprint)
        db.init_app(app)