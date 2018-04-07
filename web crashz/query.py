from models.service import Service
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
