#!/Users/IRPHAN/AppData/Local/Programs/Python/Python39/python
import cgi
import sqlite3
import re

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

def countDigits(value):
	counter = 0
	for p in value:
		if p.isdigit():
			counter +=1
	return counter

printHeader("Register")


print("""
		<div class="header">
            <img src="static/homePageLogo.jpg" alt="Logo" class="logo" onclick="window.location='index.html'"/>
            <h1>Register Page</h1>
        </div>

	    <br><br>

		<div class="darkGreenArea">
    """)


form = cgi.FieldStorage()

message = ""
warning = False

if "userName" not in form.keys():
	message ="Username should be entered!"
	warning = True
elif "password" not in form.keys():
	message ="Password should be entered!"
	warning = True
elif "passwordAgain"not in form.keys():
	message = "Password should be re-entered!"
	warning = True
elif "name"not in form.keys():
	message = "Full name should be entered"
	warning = True
elif form["password"].value != form["passwordAgain"].value:
	message= "Passwords should be the same!"
	warning = True
elif len(form["password"].value) <= 7:
	message= "Password should include at least 8 chars!"
	warning = True
elif countDigits(form["password"].value) < 2:
	message= "Password should include at least 2 digits!"
	warning = True
elif not re.match(r'[^@]+@[^@]+.[^@]+', form["email"].value):
	message= "Please enter valid email!"
	warning = True
else:
	conn = sqlite3.connect("rentHouse.db")
	c = conn.cursor()
	c.execute("SELECT * FROM USER WHERE userName = ?", (form["userName"].value,))
	row = c.fetchone()
	if row != None:
		message = "User is already in the database"
		warning = True
	else:
		c.execute("INSERT INTO USER VALUES (?, ?, ?, ?,?,?)", (form["userName"].value, form["password"].value, form["name"].value, form["email"].value,form["phoneNo"].value,0))
		message = "User is added into the database"
		conn.commit()
	conn.close()

if warning:
	print("""	<h1 style='color:red';> Warning! </h1><br><br>
				<h2 style='color:red';> {}</h2>
				<button id="log" onclick="window.location='index.html'"> Return Home</button>
			</div>
		""".format(message))
else:
	print("""	<h1 style='color:green;'> Succesful </h1><br><br>
				<h2 style='color:green';> {}</h2>
				<button id="log" onclick="window.location='index.html'"> Return Home</button>
			</div>
		""".format(message))


printFooter()
