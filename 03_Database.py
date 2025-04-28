import mysql.connector
mydb = mysql.connector.connect(host= "localhost", user= "viral", passwd= "Vir@24")
mycursor= mydb.cursor()

mycursor.execute("show Databases")
for i in mycursor:
    print(i)

