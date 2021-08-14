# MySql for mysql connection
```
pip install mysql-connector-python
```
## Connection code
```
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
```
- Using `database="demo"` is optional
- It is for using a specific database

## To create Database
```
mycursor.execute("CREATE DATABASE mydatabase")
```
- You can put any query you want
## To show database
```
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
```
## To show tables
```
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
```
## To read data from database
```
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
```
## To insert data
```
sql = "INSERT INTO new_table (name, fname) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
```
## To update
```
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()
```