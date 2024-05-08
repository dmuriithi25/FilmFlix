from connectDb import *

def addFilms():

    tblFilms = []

    # Requesting user info for new film to be added.
    title = input("Enter the film title: ")
    yearReleased = int(input("Enter the release year: "))
    rating = input("Enter the film rating (U/ G/ PG/ R): ")
    duration = int(input("Enter the film duration in minutes: "))
    genre = input("Enter the film genre: ")

    # Append/ add user entries to the films Db
    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)

    print(tblFilms)

    try:
        cursor.execute(" INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)", tblFilms)
        flixCon.commit()
        print(f"Locked in! {title} has been added to the database")
    except sql.OperationalError as e:
        flixCon.rollback() #rollback to the last time something was executed.
        print(f"Hmm. Something went wrong, that film has not been added: {e}")


if __name__ == "__main__":
    addFilms()

# Enter the Film Title: American Gangster
# Enter the Release Year: 2007
# Enter the Film Rating: 18
# Enter the Film Duration: 176
# Enter the Film Genre: Thriller 
