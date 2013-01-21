import datetime
from flask import url_for
from tumbleblog import db

class Eponyms(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    subject_name  = db.StringField(max_length=255, required=True)
    eponym_name = db.StringField(max_length=255, required=True)
    eponym_description  = db.StringField(required=True)
    references = db.StringField(required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"subject_name":self.subject_name})
    def __unicode__(self):
        return self.eponym_name

    meta = {
        'allow_inheritance' : True,
        'indexes' : ['-created_at', 'eponym_name'],
        'ordering' : ['-created_at']
    }
