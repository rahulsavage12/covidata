from flask import Flask,request
import json
import csv


j=0
def data():
    csvfile=open('data.csv','r')
    fieldnames=("SL","NAME","RELATION","AGE","DATE",'UNIT','DOORNO','ADDRESS','STATUS','DISCHARGE DATE')
    reader=csv.DictReader(csvfile,fieldnames)
    out=json.dumps([row for row in reader])
    
    return out
    



app=Flask(__name__)

@app.route('/',methods=['GET'])
def covid_cases():
    
    return (data())

if __name__ == '__main__':
    app.run()

