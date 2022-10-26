from config.database_data import create_db_connection
from utils.feed_database_from_json import (
    load_drivers_europe_json,
    load_cars_europe_json,
    insert_driver_data_into_driver_table,
    insert_car_data_into_car_table
)
from queries_test.queries import read_query


def create_all_tables():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    mycursor = connection.cursor()

    # create tables if not exist
    mycursor.execute("CREATE TABLE IF NOT EXISTS spain_drivers(id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS france_drivers (id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY (id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS germany_drivers (id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY (id))")

    mycursor.execute("CREATE TABLE IF NOT EXISTS spain_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES spain_drivers(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS france_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES france_drivers(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS germany_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES germany_drivers(id))")
    

def create_tables_all_process():
    #create and feed tables
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    
    create_all_tables()
    
    # Prevent insert duplicated data into tables
    check_if_table_is_empty_query ="""SELECT * FROM spain_cars"""
    result = read_query(connection,check_if_table_is_empty_query)
    
    if len(result) == 0 :
        data_drivers = load_drivers_europe_json()
        insert_driver_data_into_driver_table(data_drivers)
        data_cars = load_cars_europe_json()
        insert_car_data_into_car_table(data_cars)