from modules.book_management import list_books,add_book,update_book,delete_book,save_books
from database.db_setup import initialize_database
from modules.user_management import add_user_or_admin, list_users,verify_user
from modules.checkout_management import CheckoutManagement
from datetime import datetime, timedelta
from storage import Storage
from loguru import logger
import sys
from utils.utils import add_checkouts_new,update_new_checkout,add_book_new,update_new_book
# Configure logging

logger.add(sys.stdout, level="INFO")  # Log to the console


store=Storage()

checkout_manager= CheckoutManagement()


def main_menu_admin():
    """Display the main menu and return the user's choice."""
 
    print("1. List Books")
    print("2. Add Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Add user or admin")
    print("6. List Checkouts")
    print("7. Add Checkout")
    print("8. Update Checkout")
    print("9. Delete Checkout")
    print("10. List Users")
    return input("Enter your choice: ")



def main_menu_user():
    
    print("1.List Books")
    print("2.Reserve Books")
    
    return input("Enter your choice: ")




def main():
    # Create an instance of BookManagement
    try:
        logger.info("Initializing database...")
        connection = initialize_database()
        
        if connection:
            logger.info("Database initialized successfully.")
        else:
            logger.error("Database initialization failed.")
            return
        
        role = input("Enter the role of the user (admin/user): ").strip()
        id = int(input("Enter the id of the user: "))
        password = input("Enter the password of the user: ").strip()

        logger.info(f"User {id} trying to log in as {role}.")
        verified_role = verify_user(role, id, password)

        if verified_role == 'admin':
            logger.info("Admin verified")
            
            
            
    
    #     else:
    #         logger.error("Invalid credentials.")
    #         print("Invalid credentials. Access denied.")
    # except Exception as e:
    #     logger.exception(f"An error occurred: {e}")

            print('\n\n\n')  
            print("Admin verified")
          
            print('\n\n\n')
         
         
         
            print("<------------------------------------------------------------>")
         
         
            print('\n\n\n\n')
         
         
            print("Welcome to the Library Management System")
         
          
            choice= main_menu_admin()
            if choice == '1':
               filename = input("Type Books.csv to know the books in the library: ")
               list_books(filename)

            elif choice == '2':
                add_book_new()

            elif choice == '3':
               update_new_book()

            elif choice == '4':
              book_id = int(input("Enter book ID to delete: "))
              filename= input("Type Books.csv to delete from the file ")
              delete_book(book_id,filename)

            elif choice == '5':
              id = int(input("Enter the ID: "))
              name = input("Enter the name ")
              password = input("Enter the password ")
              role = input("Enter the role")
              add_user_or_admin(id,name,password,role)

            elif choice == '6':
              filename = input("Type Checkout.csv to load checkouts from the file: ")
              checkout_manager.list_checkouts(filename)

            elif choice == '7':
              
              add_checkouts_new()
              
            elif choice == '8':
              update_new_checkout(id)

            elif choice=='9':
              book_id = int(input("Enter book ID to delete: "))
              filename= input("Type Checkout.csv to delete from the file ")
              checkout_manager.delete_checkouts(book_id,filename)
            elif choice == '10':
                list_users()
            else:
                print("Invalid choice. Please try again.")
             
    
        elif verified_role == 'user':
            logger.info(f"User {id} verified")
        
        
            print("Hi Student:"+"        "+str(id))
        
            print('\n\n\n')
        
            print("<------------------------------------------------------------>")
        
            print('\n\n\n\n')
        
            print("Welcome to the Library Management System")
            choice=main_menu_user()
        
            if choice=='1':
               filename = input("Type Books.csv to know the books in the library: ")
               list_books(filename)
    
    
            if choice=='2':
        # Call the function to handle the checkout
             add_checkouts_new(id)
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        
         
        


if __name__ == "__main__":
    main()
