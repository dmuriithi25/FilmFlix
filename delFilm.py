from connectDb import *

def delFilms():

    delFilmID = int(input("If you're sure, enter the film ID you want to delete: "))
        
    # if delFilmID: #not in filmID
    #     print(f"I don't seem to recognise that {delFilmID}. Please enter a valid film ID: ")
    #     delFilms()
    #     return
    
    try:
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = '{delFilmID}'")
        flixCon.commit()
        print(f"Sad to see it go, but {delFilmID} has been DELETED.")

    except sql.OperationalError as e:
        flixCon.rollback() #rollback to the last time something was executed.
        print(f"Hmm, I can't seem to find that film in the database: {e}")

if __name__ == "__main__":

    delFilms()

        

