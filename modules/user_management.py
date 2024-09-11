from database.db_helper import execute_query, fetch_query
from loguru import logger

# Configure logging 
logger.add("logs/system.log", format="{time} {level} {message}", level="ERROR", rotation="10 MB")


def add_user_or_admin(id, name, password, role):
    #Allows only an admin to add a new user or admin.
    try:
        # Log the attempt to add a user/admin
        logger.info(f"Attempting to add {role} '{name}' with ID {id}.")
        
        # Query for inserting a new user or admin
        query = "INSERT INTO users (name, password, role) VALUES (?, ?, ?)"
        execute_query(query, (name, password, role))
        
        logger.info(f"{role.capitalize()} '{name}' added successfully with ID {id}.")
        print(f"{role.capitalize()} '{name}' added successfully.")
    
    except Exception as e:
        logger.error(f"Error adding user/admin {name} with ID {id}: {e}")
        print("An error occurred while adding the user/admin.")
        

def list_users():
    #List all users in the database.
    try:
        logger.info("Attempting to list all users.")
        query = "SELECT id, name, role FROM users"
        users = fetch_query(query)
        
        if not users:
            logger.info("No users found in the database.")
            print("No users found.")
        else:
            logger.info(f"Found {len(users)} users.")
            for user in users:
                print(f"User ID: {user[0]}, Name: {user[1]}, Role: {user[2]}")
    except Exception as e:
        logger.error(f"Error listing users: {e}")
        print("An error occurred while listing users.")
        

def verify_user(role, id, password):
    
    #Verify user credentials.
    try:
        logger.info(f"Attempting to verify user with ID {id}.")
        
        query = "SELECT * FROM users WHERE id = ? AND password = ?"
        result = fetch_query(query, (id, password))
        
        if not result:
            logger.warning(f"Invalid credentials for user ID {id}.")
            print("Invalid user ID or password.")
            return False
        elif result[0][3] != role:
            logger.warning(f"Permission denied for user ID {id}. Invalid role '{role}'.")
            print("Permission denied. Invalid role.")
            return False
        elif result[0][2] == password and result[0][3] == 'admin':
            logger.info(f"User ID {id} verified as admin.")
            return "admin"
        elif result[0][2] == password and result[0][3] == 'user':
            logger.info(f"User ID {id} verified as user.")
            return "user"
        
        
    except Exception as e:
        logger.error(f"Error verifying user with ID {id}: {e}")
        print("An error occurred while verifying user credentials.")
        return False
