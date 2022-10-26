from utils.create_tables import create_table_car_spain
from config.database_data import create_db_connection
from utils.feed_database_from_json import (
    load_drivers_europe_json,
    load_cars_europe_json,
    insert_driver_data_into_driver_table,
    insert_car_data_into_car_table
)
from queries_test.queries import (
    read_query,
    execute_query
    )

import pandas as pd    

if __name__ == '__main__':
    # create database if not exists
    # mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS bnzsa")
    
    #create tables
    """
    create_table_car_spain()
    data_drivers = load_drivers_europe_json()
    insert_driver_data_into_driver_table(data_drivers)
    data_cars = load_cars_europe_json()
    insert_car_data_into_car_table(data_cars)
    """
    #1.1 - Select simple
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")

    simple_query= """
    SELECT spain_drivers.full_name FROM spain_drivers JOIN spain_cars 
    WHERE spain_drivers.age > 25 AND spain_cars.color ="Red"; 
    """
    result = read_query(connection, simple_query)
    print(result)

    # 1.2 - Select avanzado
    """Teniendo en cuenta que un coche puede no estar asignado a nadie.
    Escribe una query que devuelva las matrículas [plate] de los coches y el nombre del conductor al que ese coche esté asignado [full_name] en toda Europa:"""
    advanced_query="""
    SELECT spain_cars.plate,spain_drivers.full_name from spain_cars JOIN spain_drivers WHERE spain_cars.driver_id = spain_drivers.id UNION SELECT france_cars.plate,france_drivers.full_name from france_cars JOIN france_drivers WHERE france_cars.driver_id = france_drivers.id UNION SELECT germany_cars.plate,germany_drivers.full_name from germany_cars JOIN germany_drivers WHERE germany_cars.driver_id = germany_drivers.id
    """
    result_advanced = read_query(connection, advanced_query)
    print(result_advanced)

    # 1.3 - Create
    """
    Crea una tabla en la que se pueda almacenar la información obtenida con el SELECT anterior:
    First step -> create europe_drivers_cars table to contain plate and driver_full_name fields.
    Second step -> Insert into europe_drivers_cars table the query results .
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS europe_drivers_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), driver_full_name VARCHAR(255), PRIMARY KEY (id))
    """
    execute_query(connection=connection, query=create_table_query)
    advanced_query_insert="""
    INSERT INTO europe_drivers_cars(plate,driver_full_name) SELECT spain_cars.plate,spain_drivers.full_name from spain_cars JOIN spain_drivers WHERE spain_cars.driver_id = spain_drivers.id UNION SELECT france_cars.plate,france_drivers.full_name from france_cars JOIN france_drivers WHERE france_cars.driver_id = france_drivers.id UNION SELECT germany_cars.plate,germany_drivers.full_name from germany_cars JOIN germany_drivers WHERE germany_cars.driver_id = germany_drivers.id
    """
    result_advanced_insert = execute_query(connection, advanced_query_insert)
    
    # 2.1 Utf
    # CREATE DATABASE bnzsa  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

    # 2.2 Dataframe
    df = pd.read_sql(advanced_query, con=connection)
    # print(df)
    countries = ["spain","spain","spain","france","france","france","germany","germany","germany"]
    df["countries"] = countries
    print(df)


