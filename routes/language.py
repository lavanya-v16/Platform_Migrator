
import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

language_route=Blueprint("language_route",__name__)

@language_route.route("/language",methods=["GET"])
def language_conversion_route():
    conversion="lang"
    return render_template("dummy.html", conversion_choice=conversion,file_type='initial')
