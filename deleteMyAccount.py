#!/usr/bin/python3
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

printHeader("Rent House | Delete Account")

print(""" <div class="header">
                <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
                <h1>Delete Account</h1>
          </div>

    """)


if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    if "session" in cookie.keys():
        
        

        conn = sqlite3.connect("rentHouse.db")
        c = conn.cursor()
        c.execute("SELECT * FROM USER WHERE sessionID= ? ",(cookie["session"].value,))
        row = c.fetchone()
        if row!=None:
            message="""<div class="darkGreenArea">
                        <h1 style='color:green;'> Succesful </h1><br><br>
		                <h2 style='color:green';> Your account was deleted!</h2> 
		                <button id="log" onclick="window.location='index.html'"> Return Home</button>
		            </div>"""
            c.execute("delete from user where sessionID= ?",(cookie["session"].value,))
            conn.commit()
        else:
            message = """<div class="darkGreenArea">
                        <h1 style='color:red;'> Warning</h1><br><br>
                        <h2 style='color:red;'> No Matching User</h1>

                    </div>"""
    else:
        message = """<div class="darkGreenArea">
                        <h1 style='color:red;'> Warning</h1><br><br>
                        <h2 style='color:red;'> Login Required</h1>

                    </div>"""

    conn.close()

else:
    message = """<div class="darkGreenArea">
                        <h1 style='color:red;'> Warning</h1><br><br>
                        <h2 style='color:red;'> Login Required</h1>

                    </div>"""

print(message)


printFooter()
    

            
		
