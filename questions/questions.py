from config.database_data import create_db_connection
from queries_test.queries import (
    read_query,
    execute_query
    )
import pandas as pd


def question_1_1():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")

    simple_query= """SELECT spain_drivers.full_name FROM spain_drivers 
    INNER JOIN spain_cars ON spain_drivers.age > 25 AND spain_cars.driver_id = spain_drivers.id AND spain_cars.color = "Red";"""
    result = read_query(connection, simple_query)
    question_str = "Select simple -> Escribe una query que devuelva todos los conductores de más de 25 años en España con un coche rojo:"
    print(f"1.1. Question: {question_str}\nAnswer: {simple_query}\n\nResult:{result}\n")
    

def question_1_2():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    question_str = """Teniendo en cuenta que un coche puede no estar asignado a nadie.
    Escribe una query que devuelva las matrículas [plate] de los coches y el nombre del conductor al que ese coche esté asignado [full_name] en toda Europa:"""
    advanced_query="""SELECT spain_cars.plate,spain_drivers.full_name from spain_cars JOIN spain_drivers WHERE spain_cars.driver_id = spain_drivers.id
    UNION SELECT france_cars.plate,france_drivers.full_name from france_cars JOIN france_drivers WHERE france_cars.driver_id = france_drivers.id 
    UNION SELECT germany_cars.plate,germany_drivers.full_name from germany_cars JOIN germany_drivers WHERE germany_cars.driver_id = germany_drivers.id"""
    result_advanced = read_query(connection, advanced_query)
    print(f"1.2. Question: {question_str}\nAnswer: {advanced_query}\n\nResult:{result_advanced}\n")


def question_1_3():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    question_str = """Crea una tabla en la que se pueda almacenar la información obtenida con el SELECT anterior:"""
    create_table_query = """CREATE TABLE IF NOT EXISTS europe_drivers_cars (id INT NOT NULL AUTO_INCREMENT, plate VARCHAR(100), driver_full_name VARCHAR(255), PRIMARY KEY (id))"""
    execute_query(connection=connection, query=create_table_query)
    print(f"1.3. Question: {question_str}\nAnswer: {create_table_query}\n")
    

def question_1_4():
    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    question_str = """Modifica la query del punto 1.2 para que inserte directamente los resultados en la tabla creada en el punto 1.3:"""
    advanced_query_insert="""INSERT INTO europe_drivers_cars(plate,driver_full_name)
    SELECT spain_cars.plate,spain_drivers.full_name from spain_cars JOIN spain_drivers WHERE spain_cars.driver_id = spain_drivers.id 
    UNION SELECT france_cars.plate,france_drivers.full_name from france_cars JOIN france_drivers WHERE france_cars.driver_id = france_drivers.id 
    UNION SELECT germany_cars.plate,germany_drivers.full_name from germany_cars JOIN germany_drivers WHERE germany_cars.driver_id = germany_drivers.id"""
    execute_query(connection=connection, query=advanced_query_insert)
    print(f"1.4. Question: {question_str}\nAnswer: {advanced_query_insert}\n")

def question_2_1():
    question_str ="""2.1 - Corrección de tipografía y estandarizado
        Escribe una porción de código o explica una posible solución que sea capaz de corregir los errores tipográficos o de codificación presentes la base de datos.
        (Puedes asumir que Beno𖡄t=Benoît y que G𖡄nther M𖡄ller = Günther Müller)."""
    answer = """When we create the database for the first time we can use this command:
    CREATE DATABASE bnzsa  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"""
    print(f"2.1. Question: {question_str}\nAnswer: {answer}\n")

def question_2_2():
    question_str ="""2.2 - Identificación de patrones
    Escribe una porción de código o explica una posible solución que añada una columna extra al DataFrame, indicando a qué país corresponde cada registro."""
    
    answer_str = """In this case creating a list containig countries and adding it to the dataframe:
    - countries = ["spain","spain","spain","france","france","france","germany","germany","germany"]
    - df["countries"] = countries"""

    advanced_query="""SELECT spain_cars.plate,spain_drivers.full_name from spain_cars JOIN spain_drivers WHERE spain_cars.driver_id = spain_drivers.id
    UNION SELECT france_cars.plate,france_drivers.full_name from france_cars JOIN france_drivers WHERE france_cars.driver_id = france_drivers.id 
    UNION SELECT germany_cars.plate,germany_drivers.full_name from germany_cars JOIN germany_drivers WHERE germany_cars.driver_id = germany_drivers.id"""

    connection = create_db_connection(host_name="localhost",user_name="mankat",user_password="0xfa0xff",db_name="bnzsa")
    
    df = pd.read_sql(advanced_query, con=connection)
    countries = ["spain","spain","spain","france","france","france","germany","germany","germany"]
    df["countries"] = countries
    print(f"1.2. Question: {question_str}\nAnswer: {answer_str}\n\nResult:{df}\n")