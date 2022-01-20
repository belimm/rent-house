#!/usr/bin/python3
import cgi
import http.cookies as Cookie
import random
import os
import sqlite3

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


printHeader("Logout Process")



if "HTTP_COOKIE" in os.environ:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    if "session" in cookie.keys():
        
        print("""
		<div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
            <h1>See You Again</h1>
        </div>

        

		<br><br>
	""")

        conn = sqlite3.connect("rentHouse.db")
        c = conn.cursor()
        c.execute("SELECT * FROM USER WHERE sessionID= ? ",(cookie["session"].value,))
        row = c.fetchone()
        if row!=None:
            c.execute("UPDATE USER SET sessionID= 0 WHERE username = ? ",(row[0],))
            conn.commit()

            message = """<script>
                            document.cookie ='session; expires=Thu, 01 Jan 1970 00:00:00 UTF; path=/;';
                        </script>

                        <div class="darkGreenArea">
                            <h1 style='color:green;'> Successful </h1><br><br>
		                    <h2 style='color:green';> Logout Successful</h2> 
		                <button id="log" onclick="window.location='index.html'"> Return Home</button>
		            </div>
                    """

        else:
            message ="""<div class="darkGreenArea">
						<h1 style='color:red';> Warning! </h1><br><br>
						<h2 style='color:red';> No Matching User!</h2> 
						<button id="log" onclick="window.location='index.html'"> Return Home</button>
				</div>
				"""
        conn.close()
    else:
         message ="""<div class="darkGreenArea">
						<h1 style='color:red';> Warning! </h1><br><br>
						<h2 style='color:red';> Login Required!</h2> 
						<button id="log" onclick="window.location='index.html'"> Return Home</button>
				</div>
				"""
else:
     message ="""<div class="darkGreenArea">
						<h1 style='color:red';> Warning! </h1><br><br>
						<h2 style='color:red';> Login Required!</h2> 
						<button id="log" onclick="window.location='index.html'"> Return Home</button>
				</div>
				"""

print(message)


printFooter()