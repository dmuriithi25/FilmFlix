from connectDb import *

def readFilms():
    try:
        cursor.execute("SELECT * FROM tblFilms")
        row = cursor.fetchall()

        for films in row:
            print(films)

    except sql.OperationalError as e:
        print(f"Hmm, I can't seem to find that film in the database: {e}")
    
if __name__ == "__main__":
    
    readFilms()