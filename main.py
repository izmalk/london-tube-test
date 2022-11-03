import mysql.connector
from mysql.connector import Error

# Output design options
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = U = '\033[4m'
    END = '\033[0m'


# Looking for a name of the line for the chosen station name
def check_station(station):
    try:
        # Connecting to DB
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='tube')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server!!! Version: ", db_Info)
            cursor = connection.cursor()

            query = 'SELECT stations.name, joins.line FROM stations INNER JOIN joins ON stations.id = ' \
                    'joins.station_id where stations.name = %s '

            # Station name prepared for the request
            value = (station,)

            cursor.execute(query, value)

            records = cursor.fetchall()
            for record in records:
                # The answer
                print(color.YELLOW + "Station: " + color.U + record[0] + color.END + " is on the " + color.RED
                      + "line: " + color.U + record[1] + color.END)
                return

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

# Top level procedure. CLI and user input goes here
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
            print(color.RED + "Invalid input. lease try again" + color.END)
            quit()
        print("Thank you for using our service! Have a pleasant journey.")
    elif c == 2:
        line_input = input("Please type in exact name of the line: ")
        print("Thank you for using our service! Have a pleasant journey.")
    else:
        print(color.RED + "Invalid input. lease try again" + color.END)
        quit()
