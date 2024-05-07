from flask import Flask, redirect, render_template, request, session, url_for
from time import strftime, time
import pandas as pd
from statistics import mode
import requests
import mysql.connector as mysql 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
db = mysql.connect(host = os.getenv('HOST'), port = os.getenv('PORT'), user = os.getenv('USER'), password = os.getenv('PASSWORD'))
cursor = db.cursor()

def TrafficLights():
    rank = 0
    cursor.execute("SELECT * FROM `dbmaster`.weather")
    myresult = cursor.fetchall()
    db.commit()
    temp = float(myresult[0][1])
    humidity = int(myresult[0][2])
    cloud = int(myresult[0][3])
    moon = int(myresult[0][4])
    #rank tempurature 
    if temp >= 16 and temp <= 35:
        rank += 1
    if temp >= 36 and temp <= 44:
        rank += 2
    if temp >= 6 and temp <= 15:
        rank += 2
    if temp >= 45:
        rank += 3
    if temp <= 5:
        rank += 3
    #rank humidity
    if humidity >= 20 and humidity <= 80:
        rank += 1
    if humidity >= 6 and humidity <= 19:
        rank += 2
    if humidity >= 81 and humidity <= 94:
        rank += 2
    if humidity >= 0 and humidity <= 5:
        rank += 3
    if humidity >= 95 and humidity <= 100:
        rank += 3
    #rank cloud percentage
    found = False
    for i in range(10):
        if found == False:
            for x in range(10):
                if found == False:
                    num = int(i * 10) + x
                    if cloud == num:
                        found = True
                if rank == 10 and cloud == 100:
                    found = True
            rank += 1
    #rank moon percentage
    found = False
    for i in range(10):
        if found == False:
            for x in range(10):
                if found == False:
                    num = int(i * 10) + x
                    if moon == num:
                        found = True
                if rank == 10 and moon == 100:
                    found = True
            rank += 1

    # send out data based on rankings
    if rank >= 20: #rank BLACK
        vals = [temp, humidity, cloud, moon, url_for('static', filename='teacherpagefiles/traffic-light-black.png')]
        return vals 
    if rank >= 15 and rank <= 19: #rank RED
        vals = [temp, humidity, cloud, moon, url_for('static', filename='teacherpagefiles/traffic-light-red.png')]
        return vals 
    if rank >= 10 and rank <= 14: #rank YELLOW
        vals = [temp, humidity, cloud, moon, url_for('static', filename='teacherpagefiles/traffic-light-yellow.png')]
        return vals 
    if rank >= 4 and rank <= 9: #rank GREEN
        vals = [temp, humidity, cloud, moon, url_for('static', filename='teacherpagefiles/traffic-light-green.png')]
        return vals 


