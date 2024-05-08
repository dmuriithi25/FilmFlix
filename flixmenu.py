
from delFilm import *
from addFilms import *
from updtFilm import *
from readFilms import *
from filmReprt import *

def filmMenu():

    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:

        with open ('flixmenu.txt', 'r') as menuFile:
            choices = menuFile.readlines()
            for line in choices:
                print(line, end="") #end='' removes tab spacing after each line.
            options = input("\n Enter a menu Option: ")

            if options not in ["1", "2", "3", "4", "5", "6"]:
                print(f"Hmmm. {options}doesn't seem like a valid option. Please enter a valid option")
                return options
         

def mainMenu():
    main = True

    while main:
        mainMenu = filmMenu()

        if mainMenu == "1":
            addFilms()
        if mainMenu == "2":
            delFilms()
        if mainMenu == "3":
            updFilms()
        if mainMenu == "4":
            readFilms()
        if mainMenu == "5":
            report = True
            while report:
                reportMenu = reportOptions()
                if reportMenu == "1":
                    title()
                elif mainMenu =="2":
                    genre()
                elif mainMenu == "3":
                    yrReleased()
                elif mainMenu == "4":
                    rating()
                else: 
                    report = False
            print("Reports are currently unavailable. Try again in a few.")
            # reportFilms()
        elif mainMenu == "6":
            return main
        else:
            main = False
        backMain = input ("Would you like to make another change? Y/N: ")

        if backMain == "Y":
            mainMenu()
        elif backMain == "N":
            input("Press Enter to exit the main Menu:")
            return main
        

def reportOptions():
    choices = 0
    while choices not in ["1", "2", "3", "4"]:

        with open ('filmReprt.txt', 'r') as reportFile:
            selection = reportFile.readlines()
            for line in selection:
                print(line, end='')
        choices = input("Enter a Report option: ")
        if choices not in ["1", "2", "3", "4"]:
                print(f"Hmmm. {choices}doesn't seem like a valid option. Please enter a valid option")
                return choices
        
if __name__ == "__main__":

    mainMenu()