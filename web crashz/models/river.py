from mongoengine import *
import mlab


mlab.connect()


#tao collection, thiet ke database


class River(Document):

    name = StringField()
    continent = StringField()
    length = IntField()
