import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

os_route=Blueprint("os_route",__name__)

@os_route.route("/os",methods=["GET"])
def os_conversion_route():
    conversion="os"
    return render_template("dummy.html", conversion_choice=conversion)