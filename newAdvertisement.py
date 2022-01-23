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
					</head>
					<body>""".format(title))

def printFooter():
	print ("</body></html>")

printHeader("Rent House | New Advertisement")

print("""
		<div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='main.py'"/>
            <h1>New Advertisement</h1>
        </div>
        <br><br><br>
		<div class="darkGreenArea">
		
	""")



form = cgi.FieldStorage()

message = ""
warning = False
city = ''

if form["city"].value == "Lefkosa":
	city = '1'
elif form["city"].value == "Girne":
	city = '2'
elif form["city"].value == "Gazi Magusa":
	city = '3'
elif form["city"].value == "Iskele":
	city = '4'
elif form["city"].value == "Guzelyurt":
	city = '5'
elif form["city"].value == "Lefke":
	city = '6'
if "street" not in form.keys():
	message ="Street should be entered!"
	warning = True
elif "noOfBedrooms" not in form.keys():
	message = "Number of Bedrooms should be entered!"
	warning = True
elif "monthlyFee"not in form.keys():
	message = "MonthlyFee should be entered"
	warning = True
else:
	try:
		if "HTTP_COOKIE" in os.environ:
			cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
			if "session" in cookie.keys():
				conn = sqlite3.connect("rentHouse.db")
				c = conn.cursor()
				c.execute("SELECT * FROM USER WHERE sessionID = ?", (cookie["session"].value,))
				row = c.fetchone()
				if row != None:
							
					c.execute("INSERT INTO HOUSE(userName, cid, street, noOfBedrooms, monthlyFee) VALUES (?,?,?,?,?)", (row[0], city, form["street"].value, form["noOfBedrooms"].value, form["monthlyFee"].value))
					message = "User is added into the database" 
					conn.commit()
	except:
		message = "advertisements is not added into the database"
		warning = True
		conn.rollback()
	finally:
		conn.close()

if warning:
	print("""
				<h1 style='color:red';> Warning! </h1><br><br>
				<h2 style='color:red';> {}</h2>
				<button id="log" onclick="window.location='newAdvertisement.html'"> Return Home</button>
			</div>
		""".format(message))
else:
	print("""	<h1 style='color:green;'> Succesful </h1><br><br>
				<h2 style='color:green';> {}</h2>
				<button id="log" onclick="window.location='main.py'"> Return Home</button>
			</div>
		""".format(message))
printFooter()














"""<!DOCTYPE html>

<html>
    <head>
        <title>Rent House | New Advertisement</title>
        <link rel="stylesheet" type="text/css" href="static/style.css">
        <link rel="shortcut icon" type="image/jpg" href="static/tabIcon.jpg"/>
        
    </head>

    <body>
        <div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html' " />
            <h1>New Advertisement</h1>
        </div>

        <br><br><br><br>

        <div class="darkGreenArea">
            
            
            
        </div>


        
        
        
    </body>
</html>"""