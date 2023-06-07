from db_config import mysql

def getAllUsers():
    q = "select * from tblusers"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(q)
    return cursor.fetchall()

def findUserById(id):
    q = "select * from tblusers where idUser=" + str(id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(q)    
    return cursor.fetchone()

def createUser(userJson):
    firstname,lastname,user,password,yearBirthDate = userJson
    q = "INSERT INTO tblusers (firstname,lastname,user,password,yearBirthDate) VALUES ('%s','%s','%s','%s','%s')" % (firstname,lastname,user,password,yearBirthDate)