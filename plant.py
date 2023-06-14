import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root",passwd='password')
from disease import prediction as dis_pred
mycoursor=mydb.cursor(buffered=True)
mycoursor.execute("show databases;")
mycoursor.execute("use mini;")
path=input('Enter the path of the image file: ')
pdis=dis_pred(path)
print("Name of the Disease:")
mycoursor.execute("select * from dps;")

print(pdis)
print()
print("Name of the plant:")
for i in mycoursor:
    if(i[0]==pdis):
        print(i[2])
        break

mycoursor.execute("select * from dps;")

print("Organic Solution is: ")
print()
for i in mycoursor:
    if(i[0]==pdis):
        print(i[1])
