"""WHAT WE'VE DONE SO FAR"""
"""
1. Created a virtual environment with venv "python -m venv venv"
    -This creates a venv folder containing a copy of python and pip for just this project
    -Note: pip is python's package installer (for external libraries)
2. Activated the virtual environment with "./venv/Scripts/activate"
    -This should put (venv) at the front of the command line
3. Installed flask with "pip install flask"

4. Created templates in a templates folder to return html pages
5. Rendered the templates with render_template()
6. Create a requirements.txt file that will let you or others easily install packages the app needs
    -Created with: pip freeze > requirements.txt
    -Can be run with pip install -r requirements.txt
7. Added a .gitignore to make sure we don't commit our venv stuff
8. Created static folder to be used to server other local resources (css/js/images)
    - used url_for() to load static assets in html pages.
"""

#Import the Flask class from the flask module

#Create an instance of the Flask app
from flask import Flask, render_template, request # render_template loads HTML from /templates
import datetime


app=Flask(__name__)

#Define the route for a homepage:


@app.route("/")
def home():
    #Return a simple string that is valid HTML
    #return "<h1>Welcome to my Flask App!</h1>"
    # Return the home template:
    return render_template("home.html")


@app.route("/time")
def time():
     #get the current time on the server
     now = datetime.datetime.now()
     #return f"<h2>Current Server Time: {now}</h2>"

     return render_template("time.html", current_time=now)


@app.route("/form", methods=['GET', 'POST'])
def form():
     if request.method == 'POST':
          name = request.form.get('name')
          ssn = request.form.get('ssn')
          return render_template("greeting.html", name=name, ssn=ssn)
     return render_template("form.html")


if __name__ == "__main__":
     #debug = True enables automatic reload on changes and better error messages
     app.run(debug=True)