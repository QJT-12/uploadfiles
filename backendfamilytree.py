from flask  import Flask 
from flask import render_template
from flask import request
from flask import redirect 
from database import Create
from database import fetchprofiles
app = Flask(__name__)
import os

os.makedirs("uploadedimage",exist_ok=True)
@app.route("/")
def home():
    crazydata = fetchprofiles()
    return render_template("index.html", crazydata = crazydata)

@app.route("/addprofile", methods=["GET","POST"])
def addprofile():
    if request.method == "POST":
        print(request.form)
        name = request.form.get("name")
        profile = request.form.get("profile")
        uploadedfile =  request.files.get("imagename")
        uploadedfile.save("static/uploadedimage/"+ uploadedfile.filename)
        imagename =  uploadedfile.filename
        Create(name,imagename,profile)
        return redirect ("/")
    return render_template("addprofile.html")

app.run()