# from models.user import User
from models.service import Service

import mlab
from faker import Faker
from random import randint, choice
import random


mlab.connect()
fake = Faker()


# tao ra Document
for i in range(70):
    print("saving service",i+1,"...")
    new_service = Service(
    image = "http://via.placeholder.com/200x200",
    name = fake.name(),
    gender=randint(0,1),
    yob=randint(1995,2000),
    height=randint(150,180),
    phone=fake.phone_number(),
    address=fake.address(),
    description= random.choice(["ngoan hien, hieu thao","dam dang, ngot ngao","ngay tho, vo so toi","manh me, bao thu","bao dam, ahihi","yeu duoi, thu dong"]),
    measurements = random.choice(["90, 60, 90 ","100, 100 ,100 ","70,80,90","100,90,100"]))
    new_service.save()  #cach luu lai Document

# for i in range(70):
#     print("saving service",i+1,"...")
#     new_user = User(name =fake.name(),
#     gender=randint(0,1),
#     company =fake.company(),
#     job = fake.job(),
#     phone=fake.phone_number(),
#     address=fake.address())
#     status = random.choice["rảnh","bận"] #0 la nu, 1 la nam
#     new_user.save()  #cach luu lai Document
