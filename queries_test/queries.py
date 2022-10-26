from mysql.connector import Error


# Ejecuta una query de lectura de la base de datos y la devuelve
def read_query(connection, query):
    cursor = connection.cursor()
    result = "NoneFOREIGN KEY (PersonID) REFERENCES Persons(PersonID)"
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# Ejecuta una query en la base de datos
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")