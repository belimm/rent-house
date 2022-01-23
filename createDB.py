import sqlite3


def createDataBase(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS USER(
        userName TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        fullName TEXT NOT NULL,
        email TEXT NOT NULL,
        phoneNo TEXT NOT NULL,
        sessionID INTEGER DEFAULT -1
        )
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS CITY(
        cid INTEGER PRIMARY KEY,
        cname TEXT NOT NULL
        )
        """)
    

    c.execute("""CREATE TABLE IF NOT EXISTS HOUSE(
        houseid INTEGER PRIMARY KEY AUTOINCREMENT,
        userName TEXT,
        cid INTEGER,
        street TEXT NOT NULL,
        noOfBedrooms INTEGER NOT NULL,
        monthlyFee INTEGER NOT NULL,
        FOREIGN KEY (userName) REFERENCES USER(userName),
        FOREIGN KEY (cid) REFERENCES CITY(cid)
        )
        """)
    
    conn.commit()
    conn.close()

    

def insertCity(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()
    
    cities = [(1,"Lefkosa"),(2,"Girne"),(3,"Gazi Magusa"),(4,"Iskele"),(5,"Guzelyurt"),(6,"Lefke")]

    c.executemany("INSERT INTO CITY VALUES(?,?)",cities)
    conn.commit()
    conn.close()
    


def readCity(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    c.execute("SELECT * FROM CITY")
    row = c.fetchmany()

    while row!=None:
        print(row)
        row = c.fetchone()

def insertUser(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    users = [("berklim","1234","Berk Limoncu","berk.limoncu@gmail.com","+905050820997",0),("belim","1234","Berk Limoncu","berk.limoncu@gmail.com","+905338801380",0)]

    c.executemany("INSERT INTO USER VALUES(?,?,?,?,?,?)",users)
    conn.commit()
    conn.close()



def readUser(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    c.execute("SELECT * FROM USER")
    row = c.fetchmany()

    while row!=None:
        print(row)
        row = c.fetchone()

def insertHouse(dbFileName):
    conn = sqlite3.connect(dbFileName)
    c = conn.cursor()

    houses = [(1,"belim",1,"limlim",2,200),(2,"berklim",3,"turunç",1,500)]

    c.executemany("INSERT INTO HOUSE VALUES(?,?,?,?,?,?)", houses)
    conn.commit()
    conn.close()



if __name__=="__main__":
    dbFileName = "rentHouse.db"
    
    createDataBase(dbFileName) 

    
    insertCity(dbFileName)

    readCity(dbFileName)

    insertUser(dbFileName)

    readUser(dbFileName)

    insertHouse(dbFileName)



