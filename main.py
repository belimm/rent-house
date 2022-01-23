#!/Users/IRPHAN/AppData/Local/Programs/Python/Python39/python
import http.cookies as Cookie
import sqlite3
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

printHeader("Rent House | Main Page")





if "HTTP_COOKIE" in os.environ:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	if "session" in cookie.keys():
		conn = sqlite3.connect("rentHouse.db")
		c = conn.cursor()
		c.execute("SELECT * FROM USER WHERE sessionID = ?", (cookie["session"].value,))
		row = c.fetchone()
		if row != None:
			
			message= """
				<div class="header">

						<div class="headersub">
							
							<div class="dropdown">
								<button class="dropbtn">{}</button>
								<div class="dropdown-content">
									<a href="logout.py">Logout</a>
									<a href="deleteMyAccount.html">Delete My Account</a>
								</div>
							</div>

						 	
						</div>
            			<img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='main.py'"/>
            			<h1>Welcome to Rent House</h1>
				</div>
				<br><br><br>
				<div class="darkGreenArea">
					<button id="log" style="width:200px;" onclick="window.location='newAdvertisement.html'">New Advertisement </button>
					<br><br>
					<button id="log" style="width:220px;" onclick="window.location='previousAdvertisements.py'">Previous Advertisements </button>
					<br><br>
					<button id="log" style="width:220px;" onclick="window.location='allAdvertisements.py'">All Advertisements </button>

				</div>
				""".format(row[0])
			
		else:
			message ="""
						<div class="header">
							<img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
							<h1>Welcome to Rent House</h1>
						</div>

						<br><br><br>

						<div class="darkGreenArea">
                        	<h1 style='color:red;'> Warning</h1><br><br>
                        	<h2 style='color:red;'> Login Required</h1>
							<button id="log" onclick="window.location='index.html'"> Return Home</button>
                    	</div>
					"""
					
        			
				
					
			
		conn.close()
	else:
		message ="""
						<div class="header">
							<img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
							<h1>Welcome to Rent House</h1>
						</div>
						
						<br><br><br>

						<div class="darkGreenArea">
                        	<h1 style='color:red;'> Warning</h1><br><br>
                        	<h2 style='color:red;'> Login Required</h1>
							<button id="log" onclick="window.location='index.html'"> Return Home</button>
                    	</div>
					"""
else:
	message ="""
						<div class="header">
							<img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
							<h1>Welcome to Rent House</h1>
						</div>

						<br><br><br>

						<div class="darkGreenArea">
                        	<h1 style='color:red;'> Warning</h1><br><br>
                        	<h2 style='color:red;'> Login Required</h1>
							<button id="log" onclick="window.location='index.html'"> Return Home</button>

                    	</div>
					"""
	
print(message)





printFooter()