from utils.create_tables import create_tables_all_process
from utils.create_database import create_database_bnzsa
from questions.questions import(
    question_1_1,
    question_1_2,
    question_1_3,
    question_1_4,
    question_2_1,
    question_2_2

)

if __name__ == '__main__':
    # create database if not exists
    create_database_bnzsa(host_name="localhost",user_name="mankat",user_password="0xfa0xff")
    
    #create and feed tables if not exist
    create_tables_all_process()
    
    #1.1 - Select simple
    question_1_1()
    
    # 1.2 - Select advanced
    question_1_2()

    # 1.3 - Create
    question_1_3()

    # 1.4 - Modify 1.2 query
    question_1_4()
    
    # 2.1 Utf
    # Using this command: CREATE DATABASE bnzsa  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
    question_2_1()

    # 2.2 Dataframe
    question_2_2()
    
    


