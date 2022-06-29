import cx_Oracle
import csv

#main variables 
csvfile=''
host=''
port=''
dbName=''
usrname=''
PassWord=''

#DB connection
dsn_tns = cx_Oracle.makedsn(host, port, service_name=dbName)
conn = cx_Oracle.connect(user=usrname, password=PassWord, dsn=dsn_tns) 
c = conn.cursor()


with open(csvfile) as f:
    records =csv.reader(f)

    #skip csv file Header> first line
    counter=1
    for i in records:
        if counter == 1:
            counter+=1
            continue
        else:
            #set ur dersired query 
            #note that variables here 'v1,v2,v3' are just dummy for clearifing the syntax
            c.execute('query (var) VALUES (:1,:2,:3)',[v1,v2,v3])
            c.execute('commit')


conn.close()
