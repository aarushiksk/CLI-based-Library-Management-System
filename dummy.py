from database.db_helper import execute_query, fetch_query

def add_dummy_users():
    """Insert some dummy users (manually assigning IDs)."""
    users = [
        (1, 'Aarushi', '1234', 'admin'),  # Admin
        (2, 'John Doe', '1234', 'user'),  # Regular User
        (3, 'Jane Doe', '3456', 'user'),  # Regular User
    ]
    for user in users:
        execute_query("INSERT INTO users (id, name, password, role) VALUES (?, ?, ?, ?)", user)
    
    print("Dummy users added successfully.")
    
if __name__ == "__main__":
    add_dummy_users() 