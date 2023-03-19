import pandas as pd
import sqlite3
conn = sqlite3.connect('yelp.db')

url = "https://raw.githubusercontent.com/apis-jigsaw/connecting-sql-lab/main/squawk/yelp_lunch_nyc.csv"
df = pd.read_csv(url)
df.to_sql('restaurants', conn)
pd.read_sql('select * from restaurants', conn)