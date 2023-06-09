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

def createUser(fname,lname,user,password,year):
    q = "INSERT INTO tblusers (firstname,lastname,user,password,yearBirthDate) " 
    q += "VALUES ('%s','%s','%s','%s',%s)" % (fname,lname,user,password,year)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid;
    return findUserById(lastid) 

def deleteUser(userId):
    qDelUser = "delete from tblusers where idUser=" + str(userId)
    qDelUserTickets = " delete from tbltickets where idUser = " + str(userId)
    conn = mysql.connect()
    cursor = conn.cursor();
    cursor.execute(qDelUserTickets)
    cursor.execute(qDelUser)
    conn.commit()