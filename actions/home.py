from flask import Flask, render_template, redirect, url_for, Blueprint, request
    

home_action = Blueprint("home_action", __name__)

@home_action.route("/", methods=['POST'])
def perform_action():
    conversion = request.form['conversion']
    submit=request.form.get("submit_choice")
    if submit:
        print(conversion)
        if conversion=="lang":
            #print("inside home lang")
            return redirect(url_for("language_route.language_conversion_route"))
        if conversion=='db':
            #print("inside home db")
            return redirect(url_for("db_route.db_conversion_route"))
        if conversion=='os':
            #print("inside home os")
            return redirect(url_for("os_route.os_conversion_route"))
        if conversion=='viz':
            #print("inside home viz")
            return redirect(url_for("viz_route.viz_conversion_route"))
        return render_template("dummy.html", conversion_choice=conversion)
    


