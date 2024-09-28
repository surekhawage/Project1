import mysql.connector

con=mysql.connector.connect(host='localhost',database='employee',user='root',password='Mohitwage@1')

cursor = con.cursor()
sql = "insert into staff (eno, ename, esalary, eaddress) VALUES(%s, %s, %s, %s)"

delete_q = "DELETE FROM staff WHERE eno is NULL OR ename is NULL OR esalary is NULL OR eaddress is NULL"

cursor.execute(delete_q)

con.commit()
print("row delted successfully...")

cursor.execute('SELECT * FROM staff')

result = cursor.fetchall()

print(result)
# for row in result:
#     print(row)

con.close()

