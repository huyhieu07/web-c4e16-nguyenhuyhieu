from mongoengine import *
import mlab


mlab.connect()


#tao collection, thiet ke database
#Service chinh la collection

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: male, 1:female
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField() #true/ false
