import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Akhil@6789")
print(mydb)
if(mydb):
    print("Connection Successful")
else:
    print("Connection unsuccessful")
mycursor=mydb.cursor()
mycursor.execute("show databases")
mycursor.execute("Show Tables")
for tb in mycursor:
        print(tb)
mycursor.execute("select * from customer_transactions where count( Transaction Type)>10")
myresult=mycursor.fetchall()

 

for row in myresult:
    print(row)
mycursor.execute("select * from customer_transactions c1 where count(c1.TransactionType)>6 JOIN countries_info c2 ON c1.TrasactionType=c2.Entity_Key where Entity_key IN('AF','JI','PK','IS','TR',SR')
myresult=mycursor.fetchall()

 

for row in myresult:
    print(row)
mycursor.execute("select sum(Transaction_Amount(in $)) from customer_transactions")
myresult=mycursor.fetchall()

 

if myresult>=1000:
    print(row)

 

mycursor.execute("select sum(Transaction_Amount(in $)) from customer_transactions")
myresult=mycursor.fetchall()

 

if myresult>600 and myresult<=1000:
    print(row)
mycursor.execute("select sum(Transaction_Amount(in $)) from customer_transactions")
myresult=mycursor.fetchall()

 

if myresult<=500:
    print(row)

 

for row in myresult:
    print(row)
mycursor.execute("select * from customer_transactions where count( Transaction Type)>6 and ")
myresult=mycursor.fetchall()

 

for row in myresult:
    print(row)
mycursor.execute("select * from customer_transactions where count( Transaction Type)>6 and ")
myresult=mycursor.fetchall()

 

for row in myresult:
    print(row)

