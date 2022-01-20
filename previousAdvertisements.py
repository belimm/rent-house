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

printHeader("Rent House | Previous Advertisements")

print("""
		<div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
            <h1>Previous Advertisements</h1>
        </div>
        <br><br><br>

	""")

exit()

form = cgi.FieldStorage()

if "username" in form.keys() and "password" in form.keys():
	conn = sqlite3.connect("rentHouse.db")
	c = conn.cursor()
    
	c.execute("SELECT * FROM USER WHERE userName = ? AND password = ?", (form["username"].value, form["password"].value))
	row = c.fetchone()
	if row != None:
		message="""<div class="darkGreenArea">
                        <h1 style='color:green;'> Successful </h1><br><br>
		                <h2 style='color:green';> Login Successful</h2> 
		                <button id="log" onclick="window.location='index.html'"> Return Home</button>
		            </div>
				"""
		
		cookie = Cookie.SimpleCookie()
		cookie["session"] = random.randint(1,1000000)
		cookie["session"]["domain"] = "localhost"
		cookie["session"]["path"] = "/"
		c.execute("UPDATE USER SET sessionID = ? WHERE userName = ?", (cookie["session"].value, form["username"].value))
		conn.commit()
		print ("<script>")
		print ("document.cookie = '{}';".format(cookie.output().replace("Set-Cookie: ", ""))) #Seting cookie with JS
		print ("window.location = 'main.py';")
		print ("</script>")
	else:
		message ="""<div class="darkGreenArea">
						<h1 style='color:red';> Warning! </h1><br><br>
						<h2 style='color:red';> Incorrect username or password</h2> 
						<button id="log" onclick="window.location='index.html'"> Return Home</button>
				</div>
				"""
		
	conn.close()

	time.sleep(0.5)
else:

	if "HTTP_COOKIE" in os.environ:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		if "session" not in cookie.keys():
			message = "<script>window.location='asd.py</script>"
			
			
	message = """<div class="darkGreenArea">	
					<h1 style='color:red';> Warning! </h1><br><br>
				 	<h2 style='color:red';> Please enter your username or password</h2>
					 <button id="log" onclick="window.location='index.html'"> Return Home</button> 
				</div>
				"""

print(message)


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