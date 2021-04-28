from flask import Flask, request, make_response, redirect, render_template, session, url_for, jsonify
from sqlalchemy import *
import psycopg2


app = Flask(__name__)

# vars for conection
host = 'ec2-23-21-229-200.compute-1.amazonaws.com'
port = 5432
database = 'd7gruu164ccb9c'
user = 'wnqueqvjtembpa'
password = '26031c1f230a44ed03f79fefdd3aad889a61d660d42f85d415a127e4c42ddf38'


conn_str = f'postgresql://{user}:{password}@{host}/{database}'
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()


connection = psycopg2.connect(user= "wnqueqvjtembpa",
                                password= "26031c1f230a44ed03f79fefdd3aad889a61d660d42f85d415a127e4c42ddf38",
                                host= "ec2-23-21-229-200.compute-1.amazonaws.com",
                                port="5432",
                                database="d7gruu164ccb9c")


# index route
@app.route('/')
def index():    
    return 'apalabrados'


#function of query for the numbers table
@app.route('/numbers')
def numbers():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT number, accumulated FROM numbers"
    cursor.execute(postgreSQL_select_Query)
    numbers = cursor.fetchall()    
        
    return make_response(
        jsonify({
            "number/accumulated": str(numbers)
        })
    )


#function of query for the texts table
@app.route('/texts')    
def texts():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT id_t, text, initial, last FROM texts"
    cursor.execute(postgreSQL_select_Query)
    numbers = cursor.fetchall()    
        
    return make_response(
        jsonify({
            "texts, initial, last": str(numbers)
        })
    )


#function of query for the characters table
@app.route('/characters')    
def characters():
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT character FROM characters"
    cursor.execute(postgreSQL_select_Query)
    numbers = cursor.fetchall()    
        
    return make_response(
        jsonify({
            "characters": str(numbers)
        })
    )
    
    
@app.errorhandler(404)
def not_found(error):
    return '404 error'


@app.errorhandler(500)
def err_serve(error):
    return 'something happend 500'