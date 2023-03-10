import sqlite3 as sql

db = sql.connect("movieDatabase.db")
cursor = db.cursor()


def intro():
    print("\nWelcome to Movie Database of Top Action Movies ")
    print("\n")


intro()


def listMovie():
    cursor.execute("SELECT * FROM movie")
    myQuery = cursor.fetchall()
    rowCount = len(myQuery)
    if rowCount == 0:
        print("Movie Database is empty")
    else:
        print("List of all the movies with the field Id, Title, Year, Director")
    print('\n'.join(map(str, myQuery)))

    mainOption()


def addMovie():
    movieList = []
    title = input("Enter the movie title : ")
    year = int(input("Enter the year of the movie from 2000  (YYYY): "))

    # while (year not in range(start, end)):
    while (year <= 2000):
        print("Entered year is invalid")

        year = int(input("Enter the year of the movie from 2000 (YYYY): "))

    director = input("Enter the director of the movie : ")
    movieList.append(title)
    movieList.append(year)
    movieList.append(director)
    insertSQL = f"""
    INSERT INTO movie VALUES (NULL, "{movieList[0]}","{movieList[1]}","{movieList[2]}")
    """

    cursor.execute(insertSQL)
    db.commit()
    print(f"Movie {title} has been added successfully to your Movie Database")

    mainOption()


def updateMovie():

    movieID = int(input("Enter the Record ID that you want to update : "))
    try:
        cursor.execute(f"SELECT ID FROM movie WHERE ID = {movieID}")
        row = cursor.fetchall()
        for r in row:
            print(r)
        if movieID in r:
            print("1.Title")
            print("2.Year")
            print("3.Director")
            field = input("Which field you want to update ? Enter 1/2/3 : ")

            if field == "1":
                newTitle = input("Enter the title you want to update : ")
                updateSQL = f"""
                UPDATE movie SET Title = "{newTitle}" WHERE ID = {movieID}
                """
                cursor.execute(updateSQL)
                db.commit()
                print(
                    f"Field {field} has been updated successfully to your Movie Database"
                )
                mainOption()
            elif field == "2":
                newYear = int(input("Enter the year you want to update : "))
                updateSQL = f"""
                UPDATE movie SET Year = {newYear} WHERE ID = {movieID}
                """
                cursor.execute(updateSQL)
                db.commit()
                print(
                    f"Field {field} has been updated successfully to your Movie Database"
                )
                mainOption()
            elif field == "3":
                newDirector = input(
                    "Enter the director name you want to update : ")
                updateSQL = f"""
                UPDATE movie SET Director = "{newDirector}" WHERE ID = {movieID}
                """
                cursor.execute(updateSQL)
                db.commit()
                print(
                    f"Field {field} has been updated successfully to your Movie Database"
                )
                mainOption()
            else:
                print("Invalid Option")
                mainOption()

        else:
            print("ID not in Database")

    except:
        print("ID not in Database")
    mainOption()


def delMovie():

    movieID = int(input("Enter the Record ID that you want to delete  : "))
    try:

        cursor.execute(f"SELECT ID FROM movie WHERE ID = {movieID}")
        row = cursor.fetchall()
        for r in row:
            print(r)
        if movieID in r:
            cursor.execute(f"DELETE FROM movie WHERE ID = {movieID}")
            db.commit()
            print(f"Record {movieID} Deleted")

    except:
        print("ID not in Database")
        mainOption()

    mainOption()


def mainOption():
    # print("\n******************")

    print("\nMenu Options:")
    choice = 0
    list = ["1", "2", "3", "4", "5"]
    print("1. List movies")
    print("2. Add movies")
    print("3. Update movies")
    print("4. Delete movies")
    print("5. Exit")
    print("\n")

    choice = input("Enter one option from above menu : ")
    while choice not in list:
        print("Entered option not in the list")
        choice = input("Enter one option from above menu : ")

    if choice == "1":
        listMovie()
    elif choice == "2":
        addMovie()
    elif choice == "3":
        updateMovie()
    elif choice == "4":
        delMovie()
    elif choice == "5":
        exit()
        # mainOption()
    else:
        print("Invalid Option")
        print("Please enter valid option from above")
        mainOption()


mainOption()
