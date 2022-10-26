import json
from config.database_data import create_db_connection


def load_drivers_europe_json():
    drivers_file = open("docs/drivers_europe.json")
    data = json.load(drivers_file)
    return data

def load_cars_europe_json():
    drivers_file = open("docs/cars_europe.json")
    data = json.load(drivers_file)
    return data
    

def insert_driver_data_into_driver_table(data_driver):
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    mycursor = connection.cursor()
    
    for driver in data_driver:
        if driver["country"] == "Spain":
            sql = "INSERT INTO spain_drivers(full_name, age) VALUES (%s, %s)"
            val = (driver["full_name"], driver["age"])
            mycursor.execute(sql, val)

            connection.commit()

        if driver["country"] == "France":
            sql = "INSERT INTO france_drivers(full_name, age) VALUES (%s, %s)"
            val = (driver["full_name"], driver["age"])
            mycursor.execute(sql, val)

            connection.commit()

        if driver["country"] == "Germany":
            sql = "INSERT INTO germany_drivers(full_name, age) VALUES (%s, %s)"
            val = (driver["full_name"], driver["age"])
            mycursor.execute(sql, val)

            connection.commit()


def insert_car_data_into_car_table(data_car):
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    mycursor = connection.cursor()
    
    for car in data_car:
        if car["country"] == "Spain":
            sql = "INSERT INTO spain_cars(plate,brand,model,color,driver_id) VALUES (%s, %s, %s, %s, %s)"
            val = (car["plate"], car["brand"], car["model"], car["color"], car["drive_id"] )
            mycursor.execute(sql, val)

            connection.commit()
        
        if car["country"] == "France":
            sql = "INSERT INTO france_cars(plate,brand,model,color,driver_id) VALUES (%s, %s, %s, %s, %s)"
            val = (car["plate"], car["brand"], car["model"], car["color"], car["drive_id"] )
            mycursor.execute(sql, val)

            connection.commit()

        if car["country"] == "Germany":
            sql = "INSERT INTO germany_cars(plate,brand,model,color,driver_id) VALUES (%s, %s, %s, %s, %s)"
            val = (car["plate"], car["brand"], car["model"], car["color"], car["drive_id"] )
            mycursor.execute(sql, val)

            connection.commit()
