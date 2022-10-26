# bnzsa_test
This project 
* Creates a database.
* Feeds database from two json files  
    1. cars_europe.json
    2. drivers_europe.json
* Makes queries
    1. Select simple.
    2. Select advanced.
    3. Create new table.
    4. Feed this new table.
    
* Fixes some errors.

**You must go to develop branch to see the code.**

## Project structure
* bnzsa
    - config
        - database_data.py 
    - docs
        - cars_europe.json
        - drivers_europe.json
    - queries_test
        - queries.py
    - questions
        - questions.py
    - utils
        - create_database.py
        - create_tables.py
        - feed_database_from_json.py
    - main.py
