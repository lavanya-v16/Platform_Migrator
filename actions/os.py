import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

os_action=Blueprint("os_action",__name__)

@os_action.route("/os",methods=["POST"])
def os_conversion_action():
    conversion="os"
    type1 = request.form['type1']
    type2 = request.form['type2']
    prompt= request.form['command']
    f = request.files['file_upload']
    content=f.read()
    if content:
        decoded_content = content.decode('utf-8')
        prompt=decoded_content  
    submit=request.form.get("submit_os")
    answer=''
    if submit:
        answer=conversionos(type1,type2,prompt)
    return render_template("dummy.html",conversion_choice=conversion,response=answer)

def conversionos(type1,type2,prompt):
    s=type1+'to'+type2+'.json'
    completion1 = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Give equivalent command to convert to'''+ type2+''' for the given input command in '''+type1+
             '''Code: '''+prompt+
                ''' Instructions:
                1. First provide the Input command: '''+ prompt+'''.
                2. Provide the equivalent command of '''+ prompt+''' in '''+ type2+'''.
                3. Ensure that the '''+ prompt+''' is a proper command used in any OS with no errors, otherwise just mention that the command has errors and has to be corrected
                4. Check if it is feasible to perform the conversion and mention about it in one line
                5. Mention the command converted and explain its functionality
                '''
            }
        ]

    )
    answer=completion1.choices[0].message.content.strip("\t")
    return answer
