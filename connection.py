import sqlite3 as sql


db = sql.connect(
    r"G:\Merlin\Study_Material\SkillBootCamp\Projects\PythonProject\movieDatabase.db")
cursor = db.cursor()

createTable = """

CREATE TABLE movie (
    "ID" INTEGER NOT NULL UNIQUE,
    "Title" TEXT,
    "year" INTEGER,
    "Director" TEXT,
    PRIMARY KEY("ID" AUTOINCREMENT) 

)

"""
# cursor.execute(createTable)
db.commit
db.close
