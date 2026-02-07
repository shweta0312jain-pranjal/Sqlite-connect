import sqlite3 
import pandas as pd

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

table = pd.read_sql_query("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(table)