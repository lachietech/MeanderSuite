# ______________________________________________________________________________________________________________________________________________________________
# Import and call Point 
# ______________________________________________________________________________________________________________________________________________________________
from flask import Flask, redirect, render_template, request, session, url_for
from time import strftime, time
import pandas as pd
from statistics import mode
import requests
import mysql.connector as mysql
from flask_bcrypt import Bcrypt 
import teacherfinder, msw, login as log, register
from studenthub_backend import page2 as p2, studentnotifications as sn, studentpage as spage, studentplanner as sp
from teacherhub_backend import page1 as p1, pb4lpointsys as pb4l, qcaatracker as qcaa, teachernotifications as tn, teacherpage as tpage, teacherplanner as tp
from adminhub_backend import adminpage as ap
from dotenv import load_dotenv
import os

if load_dotenv():
    pass
else:
    load_dotenv("/var/www/.env")

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.getenv('SECRET_KEY')
db = mysql.connect(host = os.getenv('HOST'), port = os.getenv('PORT'), user = os.getenv('USER'), password = os.getenv('PASSWORD'))
cursor = db.cursor()


# ______________________________________________________________________________________________________________________________________________________________
# The following code is for the main welcome website
# ______________________________________________________________________________________________________________________________________________________________
@app.route('/')
def index():
    return render_template("index.html")
# ------------------------------------------------------------
# Setting up a subpage for the teacher finder project page
# ------------------------------------------------------------
@app.route('/teacherfinder')
def teacherfinderdesc():
    return render_template("mainfiles/teacherfinder.html")
# ------------------------------------------------------------
# Setting up a subpage for the student notification project page
# ------------------------------------------------------------
@app.route('/studentnotifications')
def studentnotificationsdesc():
    return render_template("mainfiles/studentnotifications.html")
# ------------------------------------------------------------
# Setting up a subpage for the student planner project page
# ------------------------------------------------------------
@app.route('/studentplanner')
def studentplannerdesc():
    return render_template("mainfiles/studentplanner.html")
# ------------------------------------------------------------
# Setting up a subpage for the teacher notifications project page
# ------------------------------------------------------------
@app.route('/teachernotifications')
def teachernotificationsdesc():
    return render_template("mainfiles/teachernotifications.html")
# ------------------------------------------------------------
# Setting up a subpage for the msw project page
# ------------------------------------------------------------
@app.route('/msw')
def mswdesc():
    return render_template("mainfiles/mswdesc.html")
# ------------------------------------------------------------
# Setting up a subpage for the pb4l points project page
# ------------------------------------------------------------
@app.route('/pb4lpoints')
def pb4lpointsysdesc():
    return render_template("mainfiles/pb4lpointsysdesc.html")
# ------------------------------------------------------------
# Setting up a subpage for the qcaa tracker project page
# ------------------------------------------------------------
@app.route('/qcaatracker')
def qcaatrackerdesc():
    return render_template("mainfiles/qcaatrackerdesc.html")
# ------------------------------------------------------------
# Setting up a subpage for the teacher planner project page
# ------------------------------------------------------------
@app.route('/personalplanner')
def personalplannerdesc():
    return render_template("mainfiles/personalplannerdesc.html")
# ------------------------------------------------------------
# Setting up a subpage for the student timetable project page
# ------------------------------------------------------------
@app.route('/studenttimetable')
def studenttimetabledesc():
    return render_template("mainfiles/studenttimetabledesc.html")
# ------------------------------------------------------------
# Setting up a subpage for the teacher timetable project page
# ------------------------------------------------------------
@app.route('/teachertimetable')
def teachertimetabledesc():
    return render_template("mainfiles/teachertimetabledesc.html")
# ------------------------------------------------------------
# Setting up the teacher project page
# ------------------------------------------------------------
@app.route('/teacherprojects')
def teacherprojects():
    return render_template("mainfiles/teacherprojects.html")
# ------------------------------------------------------------
# Setting up the student project page
# ------------------------------------------------------------
@app.route('/studentprojects')
def studentprojects():
    return render_template("mainfiles/studentprojects.html")


# ______________________________________________________________________________________________________________________________________________________________
# The security portion
# ______________________________________________________________________________________________________________________________________________________________
# ------------------------------------------------------------
# Setting up a subpage for the teacher content pack register page
# ------------------------------------------------------------
@app.route('/teachercontentpack')
def teachercontentpackdesc():
    if request.method == "POST":
        return
    if request.method == "GET":
        return render_template("mainfiles/teachercontentpack.html")
# ------------------------------------------------------------
# Setting up a subpage for the student content pack register page
# ------------------------------------------------------------
@app.route('/studentcontentpack')
def studentcontentpackdesc():
    if request.method == "POST":
        return
    if request.method == "GET":
        return render_template("mainfiles/studentcontentpack.html")
# ------------------------------------------------------------
# Setting up a subpage for the school content pack register page
# ------------------------------------------------------------
@app.route('/duluxepack')
def duluxepackdesc():
    if request.method == "POST":
        return
    if request.method == "GET":
        return render_template("mainfiles/duluxepack.html")
# Setting up a subpage for the login page
# ------------------------------------------------------------ 
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return log.login()
    if request.method == "GET":
        return render_template("mainfiles/login.html")


# ______________________________________________________________________________________________________________________________________________________________
# The following code is for the StudentHub extension
# ______________________________________________________________________________________________________________________________________________________________
# /////////
# Setting up a root page for the StudentHub extension
# /////////
@app.route('/studenthub')
def studentpage():
    if "logged_in" in session:
        if session["lvl"] == 1:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("studentpagefiles/studentpage.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the StudentHub's Timetable change Notification extension
# ------------------------------------------------------------
@app.route('/studenthub/timetablechanges')
def studentnotifications():
    if "logged_in" in session:
        if session["lvl"] == 1:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("studentpagefiles/studenttimetable.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the StudentHub's Planner extension
# ------------------------------------------------------------
@app.route('/studenthub/planner')
def studentplanner():
    if "logged_in" in session:
        if session["lvl"] == 1:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("studentpagefiles/studentplanner.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the StudentHub's Teacher finder extension
# ------------------------------------------------------------
@app.route('/studenthub/teacherfinder')
def page2():
    if "logged_in" in session:
        if session["lvl"] == 1:
            if request.method == "POST":
                return render_template("studentpagefiles/answer.html", value1=teacherfinder.findateacher(), val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
            if request.method == "GET":
                return render_template("studentpagefiles/index.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])   
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))




# ______________________________________________________________________________________________________________________________________________________________
# The following code is for the TeacherHub extension
# ______________________________________________________________________________________________________________________________________________________________
# /////////
# Setting up a root page for the TeacherHub extension
# /////////
@app.route('/teacherhub')
def teacherpage():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("teacherpagefiles/teacherpage.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the TeacherHub's Timetable change Notification extension
# ------------------------------------------------------------
@app.route('/teacherhub/timetablechanges')
def teachernotifications():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("teacherpagefiles/teachertimetable.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the TeacherHub's Planner extension
# ------------------------------------------------------------
@app.route('/teacherhub/planner')
def teacherplanner():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("teacherpagefiles/teacherplanner.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the TeacherHub's Teacher finder extension
# ------------------------------------------------------------
@app.route('/teacherhub/teacherfinder', methods=["GET", "POST"])
def page1():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return render_template("teacherpagefiles/answer.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4], value1=teacherfinder.findateacher())
            if request.method == "GET":
                return render_template("teacherpagefiles/index.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))   
# ------------------------------------------------------------
# The following code is for the TeacherHub's Traffic light extension
# ------------------------------------------------------------
@app.route('/teacherhub/pb4lpointsys')
def pb4lpointsys():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return 
            if request.method == "GET":
                return render_template("teacherpagefiles/pb4lpointsys.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
# ------------------------------------------------------------
# The following code is for the TeacherHub's Traffic light extension
# ------------------------------------------------------------
@app.route('/teacherhub/qcaatracker')
def qcaatracker():
    if "logged_in" in session:
        if session["lvl"] == 2:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("teacherpagefiles/qcaatracker.html", val1=msw.TrafficLights()[0], val2=msw.TrafficLights()[1], val3=msw.TrafficLights()[2], val4=msw.TrafficLights()[3], val5=msw.TrafficLights()[4])
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# ______________________________________________________________________________________________________________________________________________________________
# The following code is for the AdminHub extension
# ______________________________________________________________________________________________________________________________________________________________
# /////////
# Setting up a root page for the AdminHub extension
# /////////
@app.route('/adminpage')
def adminpage():
    if "logged_in" in session:
        if session["lvl"] == 3:
            if request.method == "POST":
                return
            if request.method == "GET":
                return render_template("adminpagefiles/adminpage.html",)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))



# ______________________________________________________________________________________________________________________________________________________________
# Run the app
# ______________________________________________________________________________________________________________________________________________________________
if __name__ == '__main__':
    app.run()