import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

viz_route=Blueprint("viz_route",__name__)

@viz_route.route("/viz",methods=["GET"])
def viz_conversion_route():
    conversion="viz"
    return render_template("dummy.html", conversion_choice=conversion)