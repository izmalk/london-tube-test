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

        # Uploading stations
        """
        for record in data['stations']:
            query = "INSERT INTO stations (ID, name) VALUES (%s, %s)"
            values = (record['id'], record['name'])
            cursor.execute(query, values)
            print("Added: " + record['name'] + " " + record['id'])
        """

        # Uploading lines
        """
        for record in data['lines']:
            query = "INSERT INTO line (ID, name) VALUES (%s, %s)"
            for station_id in record['stations']:
                #print(record['name'] + " " + station)
                values = (station_id, record['name'])
                cursor.execute(query, values)
                print("Added: " + record['name'] + " " + station_id)
       """

       # Uploading connections (joins table)
       """
        
        for record in data['lines']:
            query = "INSERT INTO joins (station_id, line) VALUES (%s, %s)"
            for station_id in record['stations']:
                # print(record['name'] + " " + station)
                for record2 in data['stations']:
                    if record2['id'] == station_id :
                        # print(station_id + " = " + record2['id'] + " " + record2['name'] + " " + record['name'])
                        values = (station_id, record['name'])
                        cursor.execute(query, values)
                        print("Added: " + record['name'] + " " + station_id)
        """

        # Closing file
        f.close()

        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
