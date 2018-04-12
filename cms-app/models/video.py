from mongoengine import *
import mlab

mlab.connect()

class Video(Document):
    title = StringField()
    thumbnail = StringField()
    views = IntField()
    link = StringField()
    youtubeid = StringField()
