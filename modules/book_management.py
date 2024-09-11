import pandas as pd
from storage import Storage 
from loguru import logger 
import sys

# Initialize storage instance
storage = Storage()

# Configure logging
logger.add(sys.stdout, level="INFO")
logger.add("logs/library_system.log", format="{time} {level} {message}", level="INFO", rotation="10 MB")


def load_books(filename):
    #Load books from a file (CSV or JSON) into a DataFrame.
    
    try:
        books_df = storage.load_from_file(filename)
        if not books_df.empty:
            logger.info(f"Books loaded successfully from {filename}.")
        else:
            logger.warning(f"No books found in {filename} or invalid file format.")
        return books_df
    except Exception as e:
        logger.error(f"Error loading books from {filename}: {e}")
        return pd.DataFrame()

def list_books(filename):
    
    
    #List all available books.
    books_df = load_books(filename)
    if not books_df.empty:
        print(books_df)
    else:
        logger.warning(f"No books found to list from {filename}.")
    
def add_book(book_id, title, author, isbn, is_available, filename):
    
    #Add a new book to the collection and save the updated collection to the file.
    try:
        books_df = storage.load_from_file(filename)
        new_book = pd.DataFrame([{
            'book_id': book_id,
            'title': title,
            'author': author,
            'isbn': isbn,
            'is_available': is_available
        }])
        books_df = pd.concat([books_df, new_book], ignore_index=True)
        logger.info(f"Book '{title}' (ID: {book_id}) added successfully to {filename}.")
        print(f"Book '{title}' added successfully.")
        

        
        save_books(books_df, filename)
    except Exception as e:
        logger.error(f"Error adding book '{title}' with ID {book_id}: {e}")



def update_book(filename, book_id, field, new_value):
    
    try:
        books_df = storage.load_from_file(filename)
        
        # Check if the book exists
        
        if book_id in books_df['book_id'].values:
            
            # Update the field if it exists in the DataFrame
            
            if field in books_df.columns:
                books_df.loc[books_df['book_id'] == book_id, field] = new_value
                logger.info(f"Book ID {book_id} updated: {field} = {new_value}.")
                print(f"Book ID {book_id} updated: {field} = {new_value}.")
            else:
                logger.warning(f"Field '{field}' not found in {filename}.")
                print(f"Field '{field}' not found.")
        else:
            logger.warning(f"Book with ID {book_id} not found in {filename}.")
            print(f"Book with ID {book_id} not found.")
        

        save_books(books_df, filename)
    except Exception as e:
        logger.error(f"Error updating book ID {book_id} in {filename}: {e}")




def delete_book(book_id, filename):
    #Delete a book from the DataFrame and save the updated DataFrame to the file.
    try:
        books_df = storage.load_from_file(filename)
        
        # Check if the 'book_id' column exists and if the book exists
        if 'book_id' in books_df.columns and book_id in books_df['book_id'].values:
            
            # Delete the book by filtering out the book with the given book_id
            df = books_df[books_df['book_id'] != book_id]
            
            logger.info(f"Book ID {book_id} deleted successfully from {filename}.")
            print(f"Book ID {book_id} deleted successfully.")
        else:
            logger.warning(f"Book with ID {book_id} not found in {filename}.")
            print(f"Book with ID {book_id} not found.")
        

        save_books(df, filename)
    except Exception as e:
        logger.error(f"Error deleting book ID {book_id} from {filename}: {e}")
        


def save_books(books_df, filename):
    #Save the books DataFrame to a file
    try:
        storage.save_to_file(books_df, filename)
        logger.info(f"Books saved to {filename}.")
        print(f"Books saved to {filename}.")
    except Exception as e:
        logger.error(f"Error saving books to {filename}: {e}")
