from flask import Flask,request,render_template
import joblib
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        return (render_template("index.html",result1 = "OK",result2 = "OK"))
    else:
        return (render_template("index.html",result1 = "warning",result2 = "warning"))
if __name__ == "__main__":
    app.run()