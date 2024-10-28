import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

db_route=Blueprint("db_route",__name__)

@db_route.route("/db",methods=["GET"])
def db_conversion_route():
    conversion="db"
    return render_template("dummy.html", conversion_choice=conversion)