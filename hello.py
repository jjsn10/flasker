from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
#    return "<h1>Hello World!</h1>"


def index():
    first_name = "John"
    stuff = "this is bold text"
    favorite_pizza = ["Peperoni","Chesse","Pizza",41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza
                           )
'''
-Filters
safe
capitalize
lower
upper
title
trim
striptags
'''
#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
#    return "<h1>Hello {} !!</h1>".format(name)
    return render_template("user.html", user_name=name)

#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500