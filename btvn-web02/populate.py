from models.user import User
import mlab
from faker import Faker
from random import randint, choice


mlab.connect()
fake = Faker()



# for i in range(50):
#     print("saving service",i+1,"...")
#     new_user = User(name =fake.name(),
#     gender=randint(0,1),
#     company =fake.company(),
#     job = fake.job(),
#     phone=fake.phone_number(),
#     address=fake.address())
#     new_user.save()  #cach luu lai Document
