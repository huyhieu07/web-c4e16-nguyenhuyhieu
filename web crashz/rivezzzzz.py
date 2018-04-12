from models.river import River
from models.customer import *
import datetime
import mlab

mlab.connect()

# all_river = River.objects.filter(continent = "Africa")
# for i in range(len(all_river)):
#     print(all_river[i].name)


# all_river = River.objects.filter(continent = "S. America").filter( length__lte = 1000)
# for i in range(len(all_river)):
#     print(all_river[i].id)

# user = Customers.objects()
# print(user)

now = (datetime.datetime.now()).hour()
# print(now.hour, now.minute)
print(now)
