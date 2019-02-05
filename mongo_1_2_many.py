import pandas as pd
from flask import Flask
from flask_pymongo import PyMongo
import json

app= Flask(__name__)

app.config['MONGO_DBNAME'] = "db_name"
app.config['MONGO_URI'] = 'mongodb://localhost:27017/db_name'

mongo= PyMongo(app)

def mongo_add_data():
    data_table = mongo.db.data
    
    '''
    The below loop is intended for a dict of pandas dataframes with hundreds of thousands of rows. 
    It currently hasn't been tested for millions of rows. 
    Considering something like pickle compression for that if json isn't fast enough
    '''
    for df in range(len(key)):
        data_table.insert_one({'key_id':df,
                               'data_1':json.loads(
                                   data_dict[df][0].to_json(orient='index')),
                               #.to_json converts the Series to json 
                               #json.loads handles the bson requirments mongodb has
                               'data_2':json.loads(
                                   data_dict[df][1].to_json(orient='index')),
                               
                               'data_3':json.loads(
                                   data_dict[df][2].to_json(orient='index')),
                 
                               'data_4':json.loads(
                                   data_dict[df][3].to_json(orient='index')),
                               
                               'data_5': json.loads(
                                   data_dict[df][4].to_json(orient='index')),

                                 })

def mongo_add_key():
    key_table = mongo.db.key
    key_table.insert_one(json.loads(key.to_json(orient='index')))
    return print('tickers added to table')

def find_key():
    key_table= mongo.db.key
    key = key_table.find_one()
    return key

def find_data():
    key=find_key()
    data={}
    for i in range(len(key)):
        data_table= mongo.db.i
        #is this right?
        data[i] = data_table.find_one()
        
    return data

if __name__ == '__main__':
    mongo_add_data()
    mongo_add_key()

