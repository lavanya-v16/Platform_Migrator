import subprocess
from flask import Flask, redirect, render_template,request,Blueprint
import openai
import pandas as pd
import json
import os
import openai
from config import api_keys
openai.api_key = api_keys

language_action=Blueprint("language_action",__name__)

@language_action.route("/language",methods=["POST"])
def language_conversion_action():
    conversion="lang"
    type1 = request.form['type1']
    type2 = request.form['type2']
    input_type = request.form.get('input_type')

    if input_type == 'program':
        prompt = request.form['program']  # Get the user's input from the textarea
    elif input_type=="file_upload":
        # Handle file upload
        uploaded_file = request.files['file_upload']
        content=uploaded_file.read()
        if content:
            decoded_content = content.decode('utf-8')
            prompt=decoded_content  
 
    submit=request.form.get("submit_lang")
    answer=''
    if submit:
        answer=conversionlang(type1,type2,prompt)
    return render_template("dummy.html",conversion_choice=conversion,response=answer,file_type=input_type,input_program=prompt)

def conversionlang(type1,type2,prompt):
    print(type1,type2)
    print(prompt)
    s=type1+'to'+type2+'.json'
    completion1 = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'''Give equivalent code to convert : '''+ type1+''' code into   '''+type2+
             '''code for the program given in double quotes.
                Code:" '''+prompt+ 
                ''' " Use the following instrcutions for conversion. Instructions:

                1. If the '''+ prompt +''' is a recognizable program language but '''+ type1 +''' and '''+ prompt +''' program language are not same, print "Chosen input language and type of file are different, pls retry" and exit the program.
                    Example1: input code type given in prompt- 'Java'
                            code- def decToBinary(n):
                            binaryNum = [0] * n
                            i = 0;
                            while (n > 0): 
                                binaryNum[i] = n % 2
                                n = int(n / 2)
                                i += 1
                            for j in range(i - 1, -1, -1):
                                print(binaryNum[j], end = "")
                        n = 17
                        decToBinary(n)
                    Expected output: Chosen input language is Java but type of code is  Python, pls retry


                2. Check the feasibility of conversion of '''+ prompt +''' from '''+ type1 +''' language to '''+ type2 +''' language and mention about the feasibility conclusion it in one line as a comment
                Expected output of Feasable conversions: 1. The given Java program can be converted to corresponding Python program.
                         2. The given Javascript program can be converted to corresponding c# program.
                Expected output of not Feasable conversions:
                         1. The given Python program cannot be converted to corresponding GO program due to ......(mention the reason)
                If not feasible donot proceed and stop with this instrution.

                3. Identify the '''+ prompt +''' program language and mention it in one line as a comment
                Example: 1.If given code is in python: #Source code Langauge: Python
                         2. If given code is in C#: #Source code Langauge: C#
                
                4. If the code  '''+ prompt +''' doesnt follow the syntax of any recognizable language, but looks like english statements or gibberish or random letters and characters , print "Provided input is gibberish/english statement, provide program of any recognizable language", provide the reason for why it cannot be converted to another language and exit the program.
                
                Example1: 
                code- "ndcjdjfivkfmk"
                expected output - "Provided input is gibberish/english statement, provide program of any recognizable language" 
                In above example as ndcjdjfivkfmk isnt a R code but random characters, the expected output is "Provided input is gibberish/english statement, provide program of any recognizable language".
                
                Example2: 
                code- this is a c++ program
                expected output - "Provided input is gibberish/english statement, provide program of any recognizable language" 
                In above example as "this is a c++ program" isnt a program code but a english statement,so the expected output is "Provided input is gibberish/english statement, provide program of any recognizable language".
                
                5. Ensure that the '''+ prompt +''' is a proper code with no syntx errors, incase of errors, correct them and mention what has been corrected in comments. 
                Example1:
                code: for(int i=0;i<n;i++{
                printf("this is a loop)
                }
                Expected output: // missing closing brackets near i++ in line1, missing ';' at end of line2
                Mention these errors at the top of code in comments and provide equivalent converted code 
                
                6. Whatever text is given apart from code, use appropriate comment syntax of '''+ type2 +'''  language and comment it while converting.
                7. Provide only the equivalent code and no other explanation
                8. Start the program with import statements used in '''+ type2 +''' language
                9. Include all necessary import statements while converting.
                10. If any inbuilt function or module is used in the '''+ type1 +''' code that doesnt exist in '''+ type2 +''' language: mimic the same functionality 
                11. Include standard header files if applicable
                '''
                
            }
        ]

    )
    # with open(s, "w") as outfile:
    #     json.dump(completion1, outfile)
    # answer = completion1['choices'][0]['message']['content'].strip("\t").strip("'''")
    answer=completion1.choices[0].message.content.strip("\t").strip("'''")
    return answer