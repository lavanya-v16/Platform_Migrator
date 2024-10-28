import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

db_action=Blueprint("db_action",__name__)

@db_action.route("/db",methods=["POST"])
def db_conversion_action():
    conversion="db"
    type1 = request.form['type1']
    type2 = request.form['type2']
    prompt= request.form['query']
    #print(prompt)
    f = request.files['file_upload']
    content=f.read()
    if content:
        decoded_content = content.decode('utf-8')
        prompt=decoded_content  
    submit=request.form.get("submit3_db")
    answer=''
    if submit:
        answer=conversiondb(type1,type2,prompt)
    return render_template("dummy.html",conversion_choice=conversion,response=answer)
    

def conversiondb(type1,type2,prompt):
    s=type1+'to'+type2+'.json'
    completion1 = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
                        {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Give equivalent query to convert to'''+ type2+''' for the given input query in '''+type1+
             '''Code: '''+prompt+
                ''' Instructions:
                1. First identify the type of input query given for the conversion and mention about it in one line
                2. Check if the chosen query language and given query are of the same language, don't proceed with conversion incase of mismatch
                3. Ensure that the input is a proper query of some database query language with no errors, otherwise just mention that the query has errors and has to be corrected
                4. Check the feasibility of conversion and mention about it one line
                5. If the input and output are in same language, mention that in one line and don't convert further
                6. Convert the query to output database language
                7. Create necessary database and tables used in the query as well
                8. Handle missing functionalities by mimicking the functionalities 
                9. Any other text apart from the query has to be commented using appropriate syntax
                '''
            }
        ]
        

    )
    answer=completion1.choices[0].message.content.strip("\t")
    return answer
