import mysql.connector

con = mysql.connector.connect(host='localhost',database='college',user='root',password='Mohitwage@1')

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT(ROLL_NO INT(5) PRIMARY KEY, NAME VARCHAR(50), MOBILE_NO INT(10), ADDRESS VARCHAR(50))")

con.commit()

print("Table created..")

# insert_into_table = "INSERT INTO STUDENT()"
con.close()

