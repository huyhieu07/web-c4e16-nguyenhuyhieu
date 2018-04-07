from flask import Flask, render_template,redirect,url_for,request
import mlab
from models.service import Service
from models.customer import Customers

app = Flask(__name__)
mlab.connect()

#tao ra Document
# new_service = Service(name = "Linh Ka",yob=2002,gender=0,height=170,phone="0234642527",address="Tran Duy Hung",status=False)
# new_service.save()  #cach luu lai Document

@app.route('/customer')
def customers():
    # a = Customers.objects(gender = 0)
    a = Customers.objects.filter(gender = 0)
    k = []
    for i in range(10):
        k.append(a[i])

    return render_template("customer.html", a = k)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/search/<int:gender>")
# def search(gender):
#     all_services = Service.objects(gender = gender, address__icontains = "Hanoi")
#     return render_template("search.html", all_services = all_services)


# @app.route("/search/<id>")
# def by_id(id):
#     user = Service.objects.get(id=id)
#     return render_template("by-id.html", user = user)

#xoa doc theo id
# Service.objects(id="5ac093e2c7bd14f6abc94099").delete()

@app.route("/admin")
def admin():
    service = Service.objects()
    return render_template("admin.html", service = service)

# @app.route("/delete/<service_id>")
# def delete(service_id):
#     service_to_delete = Service.objects.with_id(service_id)
#     # Service.objects.(service_id).delete()  #cai nay no lay theo list nen sai
#     if service_to_delete is None:
#         return "khong tim thay"
#     else:
#         service_to_delete.delete()
#         return redirect(url_for('admin'))       #url_for la minh chay den 1 function
#
# @app.route("/new_service", methods =["GET","POST"]) #mac dinh cua method la GET
# def create():
#     if request.method == "GET":
#         return render_template("new_service.html")
#     elif request.method == "POST":
#         form = request.form
#         name = form["name"]
#         yob = form["yob"]
#         address = form["address"]
#         new_service = Service(name = name,
#                             yob = yob,
#                             address = address)
#
#         new_service.save()
#
#         return redirect(url_for("admin"))



if __name__ == '__main__':
  app.run(debug=True)
