from connectDb import *

def genre():
    filmGenre = input("Enter the film genre: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{filmGenre}'") #select all genres
    row = cursor.fetchall()
    for films in row:
        print(films)

def yrReleased():
    filmRelease = int(input("Enter the film the release year: "))
    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{filmRelease}'") #select all film release years
    row = cursor.fetchall()
    for films in row:
        print(films)

def rating():
    filmRating = input("Enter the film rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{filmRating}'") #select all ratings
    row = cursor.fetchall()
    for films in row:
        print(films)

def title():
    filmTitle = input("Enter the film title: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE title = {filmTitle}'") #select all film titles
    row = cursor.fetchall() 
    for films in row:
        print(films)

