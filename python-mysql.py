import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='denis1994',
    port='3306',
    database='login_user',
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE members (id int auto_increment primary key not null,f_name varchar(50),l_name varchar(50),contact varchar(10),email varchar(100),question varchar(100),answer varchar(100),password varchar(50))")
mycursor.execute("SELECT * FROM members")
myr=mycursor.fetchall()
for r in myr:
    print(r)