import time
import requests
import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

while True:
    #DB Conn
    db = mysql.connect(host = os.getenv('HOST'), port = os.getenv('PORT'), user = os.getenv('USER'), password = os.getenv('PASSWORD'))
    cursor = db.cursor()
    #calling the api and getting data
    url = os.getenv('URL1')
    querystring = {"q":"Brisbane"}
    headers = {os.getenv('HEADER1'), os.getenv('HEADER2')}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data1raw = response.json()
    data1 = data1raw["current"]
    url = os.getenv('URL2')
    querystring = {"q":"Brisbane"}
    headers = {os.getenv('HEADER1'), os.getenv('HEADER2')}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data2raw1 = response.json()
    data2raw2 = data2raw1["astronomy"]
    data2 = data2raw2["astro"]
    temp = data1["temp_c"]
    humidity = data1["humidity"]
    cloud = data1["cloud"]
    moon = data2["moon_illumination"]
    #send values to DB
    cursor.execute("DELETE FROM `Meander-secure`.weather")
    sql = "INSERT INTO `Meander-secure`.weather VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(sql, (1,temp,humidity,cloud,moon))
    db.commit()
    #log that the data has been updated 
    print("weather updated", temp,humidity,cloud,moon)
    #wait 5 minutes before re logging
    db.disconnect()
    time.sleep(300)