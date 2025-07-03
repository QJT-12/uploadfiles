from flask  import Flask 
from flask import render_template
from flask import request
from database import Create
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addprofile", methods=["GET","POST"])
def addprofile():
    if request.method == "POST":
        print(request.form)
        name = request.form.get("name")
        imagename = request.form.get("imagename")
        profile = request.form.get("profile")
        Create(name,imagename,profile)
        uploadedfile =  request.files [imagename]
        uploadedfile.save("uploadedfiles")
    return render_template("addprofile.html")

app.run()