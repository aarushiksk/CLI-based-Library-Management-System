import sqlite3
from loguru import logger
from database.db_setup import get_db_connection



# Configure logging
logger.add("logs/system.log", format="{time} {level} {message}", level="ERROR", rotation="10 MB")


def execute_query(query, params=()):
    """Execute an INSERT, UPDATE, or DELETE query on the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()  # Commit the transaction
        cursor.close()
        conn.close()
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise

def fetch_query(query, params=()):
    """Execute a SELECT query and return the results."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()  # Fetch all results
        cursor.close()
        conn.close()
        return result
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise
