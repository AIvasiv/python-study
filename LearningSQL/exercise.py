#Python App that queries data from remote MySQL database (phpMyAdmin in this case)
#mysql-connector-python - good library for work with sql
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor() # cursor object to navigate in the tabkes of database

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
result = cursor.fetchall()

if(result):
    for resultItr in result:
        print(resultItr[1])
else:
    print('No words were found')