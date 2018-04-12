from mongoengine import *
import mlab

mlab.connect()
class Order(Document):
    service = StringField()
    user = StringField()
    time = DateTimeField()
    is_accepted = StringField()
#0 là được phê duyệt, 1 là chưa được phê duyệt
