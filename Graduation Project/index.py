from flask import Flask , render_template,url_for,request
from math import sin,cos,tan,sqrt,pow
 

app=Flask(__name__)

##creating roots=links=URL
#main route
@app.route("/")

def main():
    return render_template("index.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")



@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__=="__main__":
    app.run(debug=True)