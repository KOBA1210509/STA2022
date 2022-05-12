""" from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "Hello, World!"
"""

""" from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "Hello, World!"
 
@app.route("/Miura")
def hello_miura():
    return "Hello, Miura!"
 
@app.route("/Tanaka")
def hello_tanaka():
    return "Hello, Tanaka!"
 """

""" from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"
 
@app.route("/<name>")
def hello_user(name):
    return f"Hello, {name}!"
 """

from flask import Flask
from flask import render_template
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return render_template('hello.html')

###実行構文
if __name__ == '__main__':
    app.run() 

