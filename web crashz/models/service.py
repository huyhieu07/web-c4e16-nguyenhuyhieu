from mongoengine import *
import mlab


mlab.connect()


#tao collection, thiet ke database
#Service chinh la collection

class Service(Document):
    image = StringField()
    name = StringField()
    gender = IntField() #0: male, 1:female
    yob = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    description = StringField()
    measurements = StringField()
    # status = BooleanField() #true/ false
