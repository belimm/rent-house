#!/Users/IRPHAN/AppData/Local/Programs/Python/Python39/python
import http.cookies as Cookie
import random
import sqlite3
import cgi
import time
import os

def printHeader(title):
    print ("Content-type: text/html")
    print ("")
    print ("""<html>
                    <head>
                        <title>{}</title>
                        <link rel="stylesheet" type="text/css" href="static/style.css">
                        <link rel="shortcut icon" type="image/jpg" href="static/tabIcon.jpg"/>
                      
                        
                    </head>
                    <body>""".format(title))

def printFooter():
    print ("</body></html>")

printHeader("Rent House | Previous Advertisements")

print("""
        <div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='main.py'"/>
            <h1>Previous Advertisements</h1>
        </div>
        <br><br><br>
    <div class="darkGreenArea2">
    """)

conn = sqlite3.connect("rentHouse.db")
c = conn.cursor()
c.execute("SELECT CITY.cname as city, street, noOfBedrooms,monthlyFee FROM HOUSE INNER JOIN CITY ON CITY.cid = HOUSE.cid")
table = c.fetchall()
print("""
    <table id ="preTable">
        <thead style='color:white';>
            <th>Street</th>
            <th>City</th>
            <th >Number of Bedrooms </th>
            <th>Monthly Fee</th>
            <th>Delete?</th>
         </thead>
        <tbody>
        """)  
for row in table:
   print("""
        <tr style='color:white';>
            <td>{}</th>
            <td>{}</th>
            <td>{}</th>
            <td>{}</th>
            <form method="post" name="deleteAdvertisement" action="deleteAdvertisement.py">
                <td><input type="submit"  name="btnDelete" id="log" value="Delete" style='width:80px;'>
                 </input></td>
            </form>
        </tr>
        """.format(row[1], row[0], row[2], row[3]))

print("""
        </tbody>
        </table>
        
        <h1 style='color:red';> Warning! </h1><br><br>
        <h2 style='color:red';> </h2>
        <button id="log" onclick="window.location='main.py'"> Return Home</button>
    </div>
    """) 




