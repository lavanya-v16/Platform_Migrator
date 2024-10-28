import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os

viz_action=Blueprint("viz_action",__name__)

@viz_action.route("/viz",methods=["POST"])
def viz_conversion_action():
    conversion="viz"
    type1 = request.form['type1']
    type2 = request.form['type2']
    prompt= request.form['code']
    #print(prompt)
    f = request.files['file_upload']
    content=f.read()
    if content:
        decoded_content = content.decode('utf-8')
        prompt=decoded_content  
    submit=request.form.get("submit_viz")
    answer=''
    if submit:
        answer=conversionviz(type1,type2,prompt)
    return render_template("dummy.html",conversion_choice=conversion,response=answer)

def conversionviz(type1,type2,prompt):
    s=type1+'to'+type2+'.json'
    completion1 = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Give equivalent code to convert to'''+ type2+''' for the given input code in '''+type1+
             '''Code: '''+prompt+
                ''' Instructions:
                1. First identify the input code language, check if it is a frontend language and mention about it in one line
                2. Check if the chosen code language and given code are of the same language, don't proceed with conversion incase of mismatch
                3. Ensure that the input is a proper code with no errors, otherwise just mention that the code has errors and has to be corrected
                4. Check if it is feasible to perform the conversion and mention about it in one line
                5. If the input and output are in same language, mention that in one line and don't convert further
                6. Ensure to stick to the code and give no other explanation
                7. Mimic the functionalities of input code to the output code
                8. Follow the syntax of the output language
                9. Comment all the text part apart from the code using appropriate comment syntax 
                '''
            }
        ]

    )
    answer=completion1.choices[0].message.content.strip("\t")
    return answer


