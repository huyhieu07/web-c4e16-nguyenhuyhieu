from models.river import River
from models.service import *
from models.customer import *
import mlab

mlab.connect()

# all_services = Service.object()
# print(all_services[0].name)


# id_to_find = "5ac08cfac7bd14f509f939fa"
# kieu_anh = Service.objects(id = id_to_find)[0]
# Servicez = Service.objects.with_id(id_to_find)   #ham with id la ham moi
# if kieu_anh is None:
#     print("khong thay")
# else:
#     Servicez.update(set__yob = 2003)#set-- + truong minh muon update
#     Servicez.reload()
#     print(Servicez.yob)
    # print(kieu_anh.to_mongo())

username = "admin"
password = "123"
# all_customer = Customers.objects()
# if (username in all_customer) and (password == object.password):
user = Customers.objects(username = username, password = password)
print(user[0].fullname)
# user_id = user[0].id
# session["id"] = user_id
