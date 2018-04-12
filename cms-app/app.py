from flask import *
from models.video import Video
import mlab
from youtube_dl import YoutubeDL

app = Flask(__name__)
app.secret_key = "asdkjafendaenfk"
mlab.connect()


@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html',videos=videos )


@app.route('/admin', methods =["GET","POST"])
def admin():
    if request.method == "GET":
        if "Logged_in" in session:
            videos = Video.objects()
            return render_template('admin.html', videos = videos)
        else:
            return render_template('error.html')
    elif request.method == "POST":
        form = request.form
        link = form["link"]
        ydl = YoutubeDL()
        data = ydl.extract_info(link, download=False)
        title =data["title"]
        thumbnail=data["thumbnail"]
        views = data["view_count"]
        link = data["webpage_url"]
        youtubeid = data['id']
        new_video = Video(title=title,
        thumbnail=thumbnail,
        views=views,link=link,youtubeid=youtubeid)
        new_video.save()

        return redirect(url_for("admin"))
    # return render_template("admin.html")

@app.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        if username == "admin" and password == "admin":
            session["Logged_in"] = True
            return redirect(url_for('admin'))
        else:
            return "false"
        return username + password

@app.route('/logout')
def logout():
    del session["Logged_in"]    #xoa ca key va value
    return redirect(url_for('index'))

@app.route('/detail/<videoid>')
def detail(videoid):
    return render_template("detail.html", videoid = videoid)

if __name__ == '__main__':
  app.run(debug=True)