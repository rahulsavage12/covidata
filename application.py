from flask import Flask,request
import json
import csv


j=0
def data(name):
    if(name=='rahul'):
        csvfile=open('data.csv','r')
        fieldnames=("SL","NAME","RELATION","AGE","DATE",'UNIT','DOORNO','ADDRESS','STATUS','DISCHARGE DATE')
        reader=csv.DictReader(csvfile,fieldnames)
        
    
    return json.dumps([row for row in reader])
    



application=Flask(__name__)

@application.route('/params')
def covid_cases():
    arg1=request.args['arg1']
    return (data(arg1))
   

if __name__ == '__main__':
    application.run()

