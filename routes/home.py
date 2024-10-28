import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

home_route=Blueprint("home_route",__name__)

@home_route.route("/", methods=['GET'])
def display_route():
    conversion='default'
    return render_template("dummy.html", conversion_choice=conversion)




