import mysql.connector
from mysql.connector import Error

class color:
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Looking for a name of the line for chosen station
def check_station(station):
    try:
        # Connecting to DB
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='tube')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server!!! Version: ", db_Info)
            cursor = connection.cursor()

            # query = 'SELECT * FROM stations where stations.name = %s INNER JOIN joins ON stations.id = joins.station_id'

            query = 'SELECT stations.name, joins.line FROM stations INNER JOIN joins ON stations.id = joins.station_id where stations.name = %s'

            value = (station, )

            cursor.execute(query, value)

            records = cursor.fetchall()
            for record in records:
                print("Station: " + color.UNDERLINE + record[0] + color.END + " is on the line: " + color.UNDERLINE + record[1] + color.END)


    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    print("Please choose one of the following actions: ")
    print("1 — Find line by station")
    print("2 — Find station by line")

    try:
        c = int(input("Type in the number: "))
    except Error as e:
        print("Input error", e)
        quit()

    if c == 1:
        station_input = input("Please type in exact name of the station: ")
        if station_input != '':
            check_station(station_input)
        else:
            print("Invalid input. lease try again")
            quit()
        print("Thank you for using our service! Have a pleasant journey.")
    elif c == 2:
        line_input = input("Please type in exact name of the line: ")
        print("Thank you for using our service! Have a pleasant journey.")
    else:
        print("Invalid input. lease try again")
        quit()

    # connect_db()
