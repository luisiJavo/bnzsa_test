from config.database_data import create_db_connection


def create_table_car_spain():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    mycursor = connection.cursor()

    # create database if not exists
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS bnzsa")
    
    # create tables if not exist
    mycursor.execute("CREATE TABLE IF NOT EXISTS spain_drivers(id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS france_drivers (id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY (id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS germany_drivers (id INT NOT NULL AUTO_INCREMENT, full_name VARCHAR(255), age INT, PRIMARY KEY (id))")

    mycursor.execute("CREATE TABLE IF NOT EXISTS spain_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES spain_drivers(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS france_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES france_drivers(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS germany_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), brand VARCHAR(100),model VARCHAR(100), color VARCHAR(100), driver_id INT, PRIMARY KEY (id),FOREIGN KEY (driver_id) REFERENCES germany_drivers(id))")
    