#!/Users/IRPHAN/AppData/Local/Programs/Python/Python39/python
from asyncio.windows_events import NULL
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
                        <script type="text/javascript" src="filter.js"></script>
					</head>
					<body>""".format(title))

def printFooter():
	print ("</body></html>")

printHeader("Rent House | New Advertisement")

print("""
		<div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='main.py'"/>
            <h1>All Advertisements</h1>
        </div>
        <br><br><br>
		<div class="darkGreenArea2">
		
	""")

conn = sqlite3.connect("rentHouse.db")
c = conn.cursor()
c.execute("SELECT CITY.cname as city, street, noOfBedrooms,monthlyFee, USER.email as mail, USER.phoneNo as phone FROM HOUSE INNER JOIN CITY ON CITY.cid = HOUSE.cid INNER JOIN USER ON USER.userName = HOUSE.userName ORDER BY HOUSE.houseid DESC")
table = c.fetchall()
print("""
    <table id = "adds-table">
        <thead style='color:white';>
            <th col-index = 1>Street</th>
            <th col-index = 2>City
                <select class = "table-filter" onchange = "filter_rows()">
                    <option value="all"></option>
                </select>
            </th>
            <th col-index = 3>Number of Bedrooms
                <select class = "table-filter" onchange = "filter_rows()">
                    <option value="all"></option>
                </select>
            </th>
            <th col-index = 4>Monthly Fee
                <select class = "table-filter" onchange = "filter_rows()">
                    <option value="all"></option>
                </select>
            </th>
            <th col-index = 5>Contact Email</th>
            <th col-index = 6>Contact Phone</th>

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
            <td>{}</th>
            <td>{}</th>
        </tr>
        """.format(row[1], row[0], row[2], row[3], row[4], row[5]))
print("""
        </tbody>
        </table>
        <script>
            window.onload = () => {
                document.querySelector("#adds-table>tbody>tr:nth-child(1)>td:nth-child(2)").innerHTML
            };
            
            getUniqueValuesFromColumn()

        </script>
        <br><br><br>
        <button id="log" onclick="window.location='main.py'"> Return Home</button>
    </div>
    """)  
        

printFooter()