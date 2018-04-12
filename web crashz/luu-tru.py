

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



    # khong có thang services ?
# @app.route("/search/<int:gender>")
# def search(gender):
#     all_services = Service.objects(gender = gender, address__icontains = "Hanoi")
#     return render_template("search.html", all_services = all_services)
#

#xoa doc theo id
# Service.objects(id="5ac093e2c7bd14f6abc94099").delete()


# @app.route("/search/<id>")
# def by_id(id):
#     user = Service.objects.get(id=id)
#     return render_template("by-id.html", user = user)

#################################



    # seri_id = Service.objects.get(id = service_id)
    # seri_id = Service.objects.with_id()
