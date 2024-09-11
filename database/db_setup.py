import sqlite3
import os
from loguru import logger


DATABASE_PATH = "users.db"
SQL_SCRIPTS_PATH = os.path.join("sql", "create_table.sql")


logger.add("logs/system.log", format="{time} {level} {message}", level="ERROR", rotation="10 MB")

def get_db_connection():
    #Establish a database connection.
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        return conn
    except sqlite3.Error as e:
        logger.error(f"Failed to connect to the database: {e}")
        raise

def initialize_database():
    #Initialize the database by running the create_tables.sql script.
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        with open(SQL_SCRIPTS_PATH, 'r') as sql_file:
            sql_script = sql_file.read()
        
        cursor.executescript(sql_script)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        logger.error(f"Error occurred during database initialization: {e}")
        raise
    except FileNotFoundError as fe:
        logger.error(f"SQL script file not found: {fe}")
        raise
