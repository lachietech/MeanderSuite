from flask import Flask, redirect, render_template, request, session, url_for
from time import strftime, time
import pandas as pd
from statistics import mode
import requests
import mysql.connector as mysql 
from dotenv import load_dotenv
import os

if load_dotenv():
    pass
else:
    load_dotenv("/var/www/.env")

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
db = mysql.connect(host = os.getenv('HOST'), port = os.getenv('PORT'), user = os.getenv('USER'), password = os.getenv('PASSWORD'))
db = mysql.connect(host = os.getenv('HOST'), port = os.getenv('PORT'), user = os.getenv('USER'), password = os.getenv('PASSWORD'))
cursor = db.cursor()

def findateacher():
    #setting date and time (redifine these to make it a permanant situation)
    search = request.form["name"]
    lastname = search
    date = "28/01/2021" #strftime("%d/%m/%Y")
    hour = strftime("%H")
    minute = int(strftime("%M"))
    if hour == "08":
        hour = "8"
    if hour == "09":
        hour = "9"
    # m1 (for later in the program)
    m1 = strftime("%M")
    period = ""
    #changing M1 manually so that the integers from the clock format correctly
    m1vals = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for i in range(len(m1vals)):
        if m1 == m1vals[i]:
            minute = i
    #deciding the period
    hourvals = ["8", "8", "9", "9", "10", "11", "12", "13", "14" ]
    minvals = [40, 38, 45, 45, 0, 0, 40, 0, 35]
    periodvals = ["8:30", "8:40", "8:40", "9:50", "9:50", "11:30", "11:30", "13:25", "13:25"]
    for i in range(len(hourvals)):
        if hour == hourvals[i]:
            if minute > minvals[i]:
                period = periodvals[i]
            if minute < minvals[i]:
                period = periodvals[i]
    #setting the values for room retrival 
    Date = 1
    Start_Time = 3
    Staff_Last_Name = 6
    Facility_Code = 8
    #retriving and stripping values for output
    timetable = pd.read_csv("Timetable.csv", header=None, index_col=None)
    res = timetable.loc[(timetable[Staff_Last_Name] == lastname) & (timetable[Date] == date) & (timetable[Start_Time] == period)]
    answer1 = res[Facility_Code]
    answer2 = str(answer1.values)
    resulta = answer2.strip("[']")
    result = str("In:" + resulta)
    #if no result output try again code
    if resulta == "":
        result = "Currently Out Of Class: Please Try Their Staffroom, Or Check If They Are On Lunch Duty"
    return result