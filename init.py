import mysql.connector, json
from mysql.connector import Error

try:
    # Opening JSON file
    f = open('train-network.json')
    # Connecting to DB
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database='tube')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server!!! Version: ", db_Info)
        cursor = connection.cursor()

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        # values = []
        for record in data['stations']:
            query = "INSERT INTO stations (ID, name) VALUES (%s, %s)"
            values = (record['id'], record['name'])
            cursor.execute(query, values)
            print("Added: " + record['name'] + " " + record['id'])


            # values = values.append(record['name'], record['id'])

        # Closing file
        f.close()





        #query = "INSERT INTO stations (ID, name) VALUES (%s, %s)"
        # cursor.execute(query, values)
       #cursor.executemany(query, values)
        connection.commit()
        #print(cursor.rowcount, "User added")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
