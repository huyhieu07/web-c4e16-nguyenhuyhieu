from flask import Flask, render_template
import mlab
from models.service import Service
from models.customer import Customers

app = Flask(__name__)
mlab.connect()

@app.route('/customer')
def cust():
    # a = Customers.objects(gender = 0)
    a = Customers.objects.filter(gender = 0)
    k = []
    for i in range(10):
        k.append(a[i])

    return render_template("customer.html", a = k)


##################################

#tim theo id
@app.route("/search/<id>")
def by_id(id):
    user = Service.objects.get(id=id)
    return render_template("by-id.html", user = user)

# xoa doc theo id
Service.objects(id="5ac093e2c7bd14f6abc94099").delete()

    
if __name__ == '__main__':
  app.run(debug=True)
