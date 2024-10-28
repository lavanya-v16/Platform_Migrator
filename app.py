import subprocess
from flask import Flask, redirect, render_template,request
import openai
import pandas as pd
import json
import os
from routes.home import home_route
from actions.home import home_action
from routes.language import language_route
from actions.language import language_action
from routes.db import db_route
from actions.db import db_action
from routes.os import os_route
from actions.os import os_action
from routes.viz import viz_route
from actions.viz import viz_action

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(home_action)
app.register_blueprint(language_route)
app.register_blueprint(language_action)
app.register_blueprint(db_route)
app.register_blueprint(db_action)
app.register_blueprint(os_route)
app.register_blueprint(os_action)
app.register_blueprint(viz_route)
app.register_blueprint(viz_action)

@app.route("/",methods=["GET"])
def home():
    return redirect("/home")

if __name__=="__main__":
    app.run(debug=True)