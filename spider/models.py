#-*- coding: utf-8 -*-
#from django.db import models
from mongoengine import Document, DynamicDocument, EmbeddedDocument, fields

class PageDocument(Document):
    meta = {
        'collection': 'page',
#        'db_alias': 'crawler'

    }

    url = fields.StringField()
    raw_content = fields.StringField()
    extract_content = fields.StringField()
    title = fields.StringField()
