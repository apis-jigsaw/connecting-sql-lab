from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to squawk!'

@app.route('/restaurants')
def index():
   conn = psycopg2.connect(database = 'squawk_development', password = 'postgres', user = 'postgres')
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM restaurants;')
   restaurant_records = cursor.fetchall()
   return jsonify(restaurant_records)

@app.route('/restaurants/<id>')
def show(id):
   conn = psycopg2.connect(database = 'squawk_development', password = 'postgres', user = 'postgres')
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM restaurants WHERE id = %s;', (id,))
   restaurant_record = cursor.fetchone()
   return jsonify(restaurant_record)

app.run(debug = True)
