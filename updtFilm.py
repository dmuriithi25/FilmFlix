from connectDb import *

def updFilms():

    currID = int(input("Enter the film ID for the film you want to update: "))

    filmField = input("Enter the field you want to update (Title, Year Released, Rating, Duration, Genre): ").title()

    validFields = ["Title", "Year Released", "Rating", "Duration", "Genre"]

    if filmField not in validFields:
        print(f"Hmm, I can't seem to find {filmField} in the database. Try entering a valid field: ")
        updFilms()
        return
    
    newValue = input(f"What's the new value for {filmField}?: ")

    try:
        cursor.execute(f"UPDATE tblFilms SET {filmField} = '{newValue}' WHERE filmID = {currID}")
        flixCon.commit()
        print(f"BOOM! {filmField} has been UPDATED!")

    except sql.OperationalError as e:
        flixCon.rollback() #rollback to the last time something was executed.
        print(f"Hmm. Something went wrong, that film has not been updated: {e}")

if __name__ == "__main__":
    
    updFilms()
    


