# from flask import Flask, render_template,redirect,url_for,request, session
from flask import *
import mlab
import datetime
from models.service import Service
from models.customer import Customers
from models.reference import Order
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = "dayla1doanvanbankhongcoynghia"
mlab.connect()

########################
@app.route('/')
def index():
    services = Service.objects()
    return render_template("index.html", services = services)
########################
@app.route("/admin")
def admin():
    service = Service.objects()
    return render_template("admin.html", s = service)
########################
@app.route('/sign-up', methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('sign-up.html')
    if request.method == "POST":
        form = request.form
        fullname = form['fullname']
        gmail = form['gmaill']
        username = form['username']
        password = form['password']
        new_customer = Customers(
        fullname = fullname,
        gmail = gmail,
        username = username,
        password = password,
        request = "0"
        )
        new_customer.save()
    return redirect(url_for('signin'))

########################
@app.route('/sign-in', methods = ["GET","POST"])
def signin():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        users = Customers.objects()
        user = Customers.objects(username = username, password = password)
        if len(user) == 1:
            session["Logged_in"] = True
            user_id = str(user[0].id)
            session["id"] = user_id
            # ly do la thang user_id lay ra no co type la Object_Id nen thang session no khong luu vao dc
            # em chi can chuyen no thanh 1 string la dc nhe

            # k = session['detail_id']
            # return redirect(url_for('detail', service_id = k ))
            return redirect(url_for('index'))
        else:
            flash("Sorry, but you could not log in.")
            session["Logged_in"] = False
            return render_template('error.html')
########################
@app.route('/logout')
def logout():
    del session["Logged_in"]    #xoa ca key va value
    return redirect(url_for('index'))
########################
@app.route("/new_service", methods =["GET","POST"]) #mac dinh cua method la GET
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        address = form["address"]
        height = form["height"]
        description = form["description"]
        phone = form["phone"]
        gender = form["gender"]
        measurements = form["measurements"]
        new_service = Service(name = name,
                            yob = yob,
                            address = address,
                            height=height,
                            description=description,
                            phone=phone,
                            gender = gender,
                            measurements = measurements,
                            )
        new_service.save()
        return redirect(url_for("admin"))
########################

@app.route("/update-service/<service_id>",methods =["GET","POST"])
def update(service_id):
    seri_id = Service.objects.get(id = service_id)

    if request.method == "GET":
        return render_template("update-service.html", s = seri_id) #s = service
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        address = form["address"]
        height = form["height"]
        description = form["description"]
        phone = form["phone"]
        measurements = form["measurements"]
        gender = form["gender"]

    seri_id.update(set__name = name )
    seri_id.update(set__yob = yob )
    seri_id.update(set__address = address)
    seri_id.update(set__height = height)
    seri_id.update(set__description = description)
    seri_id.update(set__phone = phone)
    seri_id.update(set__measurements = measurements)
    seri_id.update(set__gender = gender)
    seri_id.reload()
    return redirect(url_for("admin"))
########################

@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    # Service.objects.(service_id).delete()  #cai nay no lay theo list nen sai
    if service_to_delete is None:
        return "khong tim thay"
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))       #url_for la minh chay den 1 function
########################
@app.route("/detail/<service_id>")
def detail(service_id):

    if "Logged_in" in session:
        seri_id = Service.objects.get(id = service_id)
        session['detail_id'] = str(seri_id.id)
        return render_template("detail.html", hola = seri_id)
    else:
        seri_id = Service.objects.get(id = service_id)
        session['detail_id'] = str(seri_id.id)
        # kkk = session['detail_id']

        return redirect(url_for('signin'))
########################
@app.route('/order')
def order():
     seri_id = Customers.objects.get(id = session["id"])
     seri_id.update(set__request = "1")
# trạng thái của đơn
     seri_id.reload() #load lại dữ liệu
     service_object = Service.objects.get(id = str(session['detail_id']))
     service_name = service_object['name']
#lấy id, rồi lấy name dựa vào id
     user_object = Customers.objects.get(id = str(session["id"]))
     user_name = user_object['fullname']
#tạo documents cho class Order:
     new_order = Order(
     service = service_name,
     user = user_name,
     time = datetime.datetime.now(),
     is_accepted = '1'
     )
     new_order.save()
     return render_template('order-ticket.html')
########################
@app.route('/admin/order-data')
def order_data():
    order_items = Order.objects()
    return render_template('order-page.html', order_items = order_items)
def send_mail():
    user_object = Customers.objects.get(id = str(session["id"]))
    user_gmail = user_object['gmail']
    gmail = GMail('vihoabinhnhanloai@gmail.com','thisishuyhieu')

    contentz = '''
    <p>Đơn h&agrave;ng của bạn đ&atilde; được vận chuyển, cảm ơn bạn đ&atilde; tin d&ugrave;ng dịch vụ của ch&uacute;ng t&ocirc;i!!!</p>
    <p></p>
    <p>--Muadongkhonglanh--&nbsp;</p>'''
    msg = Message('Muadongkhonglanh',to = user_gmail, html = contentz)

    # don_hang = Order.objects.get(id=)
    order_items.update(set__is_accepted = "0")
    gmail.send(msg)



if __name__ == '__main__':
  app.run(debug=True)
