from flask import Flask, render_template, request


app = Flask(__name__,template_folder='templates', static_folder='static')
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root",passwd='password')
from disease import prediction as dis_pred
import smtplib, ssl

@app.route('/')
def hello():
    return render_template('contact.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    l={}

    mycoursor=mydb.cursor(buffered=True)
    mycoursor.execute("show databases;")
    mycoursor.execute("use mini;")
    path=request.form['name']
    pdis=dis_pred(path)
    print("Name of the Disease:")
    mycoursor.execute("select * from dps;")

    print(pdis)
    l["Name of the Disease"]=pdis
    print()
    print("Name of the plant:")
    for i in mycoursor:
        if(i[0]==pdis):
            print(i[2])
            l["Name of the plant"]=i[2]
            break
    mycoursor.execute("select * from dps;")

    print("Organic Solution is: ")
    print()
    for i in mycoursor:
        if(i[0]==pdis):
            print(i[1])
            l["Organic solution"]=i[1]
    s=[]
    for i in l:
        s.append(str(i+": "+l[i]))


    return '\n'.join(s)


if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()