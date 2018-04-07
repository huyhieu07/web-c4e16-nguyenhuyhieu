from mongoengine import *
import mlab


mlab.connect()


#tao collection, thiet ke database
#Service chinh la collection

class Customers(Document):
    name = StringField()
    company = StringField()
    gender = IntField() #0: male, 1:female
    phone = StringField()
    address = StringField()
    job = StringField()
