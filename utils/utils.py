from datetime import datetime, timedelta
from storage import Storage

import sys
from modules.checkout_management import CheckoutManagement
from modules.user_management import add_user_or_admin, list_users,verify_user
from modules.book_management import add_book, update_book, delete_book
checkout_manager= CheckoutManagement()
store = Storage()


def add_checkouts_new(id):
    try:
        book_id = int(input("Enter book ID: "))
        filename = input("Type Books.csv to load books from the file: ").strip()
        
        df = store.load_from_file(filename)
        
        if book_id not in df['book_id'].values:
            logger.warning(f"Book ID {book_id} not available in the library.")
            print("This book is not available in the library")
            return

        title = input("Enter title: ").strip()
        issued_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return_date = (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S')

        checkout_file = input("Type Checkout.csv to pass your book to checkout: ").strip()
        
        logger.info(f"Adding checkout for Book ID {book_id} by User ID {id}. Issued on {issued_date}, return by {return_date}.")
        checkout_manager.add_checkouts(book_id, title, issued_date, return_date, id, checkout_file)
        delete_book(book_id, filename)

        logger.info(f"Checkout for Book ID {book_id} added successfully.")
    except Exception as e:
        logger.exception(f"An error occurred while adding checkout: {e}")

    


from loguru import logger

def update_new_checkout(id):
    try:
        filename = input("Type Checkout.csv to load the checkout file").strip()
        book_id = int(input("Enter book ID to update: "))
        user_id = id
        field_to_update = input("Enter the field to update (title, author, isbn, is_available): ").strip()
        new_value = input(f"Enter the new value for {field_to_update}: ").strip()

        # Convert new_value to integer if necessary
        if field_to_update in ['book_id', 'is_available']:
            new_value = int(new_value)

        logger.info(f"User {user_id} is updating checkout for Book ID {book_id}. Field: {field_to_update}, New Value: {new_value}")

        # Update the book and save the changes
        checkout_manager.update_checkouts(filename, book_id, field_to_update, new_value, user_id)

        logger.info(f"Checkout for Book ID {book_id} updated successfully.")
    
    except ValueError as ve:
        logger.error(f"Invalid value provided by User {user_id}: {ve}")
        print(f"Invalid input. Please check the value for {field_to_update}.")
    
    except Exception as e:
        logger.exception(f"An error occurred while updating checkout for Book ID {book_id}: {e}")
        print("An unexpected error occurred. Please try again.")



def add_book_new():
    try:
        book_id = int(input("Enter book ID: "))
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        is_available = input("Is the book available? (True/False): ").strip().lower() == 'true'
        file = input("Type Books.csv to save the book to your file: ").strip()

        logger.info(f"Adding book {title} (ID: {book_id}, Author: {author}) to {file}")
        
        add_book(book_id, title, author, isbn, is_available, file)
        logger.info(f"Book {title} added successfully.")
    except ValueError as ve:
        logger.error(f"ValueError occurred: {ve}")
        print("Invalid input. Please enter correct values.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")

    
    
def update_new_book():
    filename = input("Type Books.csv to load books from the file and update them")
    book_id = int(input("Enter book ID to update: "))
    field_to_update = input("Enter the field to update (title, author, isbn, is_available): ")
    new_value = input(f"Enter the new value for {field_to_update}: ")
   
    if field_to_update in ['book_id', 'is_available']:
        new_value = int(new_value)

    # Update the book and save the changes
    update_book(filename, book_id, field_to_update, new_value)