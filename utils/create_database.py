from config.database_data import create_database_if_not_exists

def create_database_bnzsa(host_name="localhost",user_name="mankat",user_password="0xfa0xff"):
    connection = create_database_if_not_exists(host_name=host_name,user_name=user_name,user_password=user_password)
    mycursor = connection.cursor()

    # create database if not exists
    mycursor.execute("CREATE DATABASE IF NOT EXISTS bnzsa CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci")