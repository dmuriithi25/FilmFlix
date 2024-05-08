import sqlite3 as sql

try:
    with sql.connect("/Users/elishacrawford/Desktop/Just IT/Projects/Python Film Db Project/filmflix.db") as flixCon:  #conn is short for connect
        cursor = flixCon.cursor()

except sql.OperationalError as e:
    print(f"Connection Failed!, {e}")