import pandas as pd
from storage import Storage  # Assuming storage.py is in the same directory
import sys
from loguru import logger
logger.add(sys.stdout, level="INFO")
logger.add("logs/library_system.log", format="{time} {level} {message}", level="INFO", rotation="10 MB")


storage=Storage()

class CheckoutManagement:
    def __init__(self):
        #Initialize the BookManagement system with a storage object and a books DataFrame.
        
        self.storage = Storage()  
        self.checkout_df = pd.DataFrame()  

    def list_checkouts(self, filename):
        
        #Load books from a file (CSV or JSON) into a DataFrame.
        logger.info("Loading books...")
        self.checkout_df = self.storage.load_from_file(filename)
        if not self.checkout_df.empty:
            print("Books loaded successfully!")
            print(self.checkout_df)
        else:
            logger.warning("No books found or invalid file format.")
            print("No books found or invalid file format.")


    def add_checkouts(self, book_id, title, issued_date, return_date, user_id, filename):
        
     #Add a new book to the collection and save the updated collection to the file.
     logger.info(f"Adding book '{title}' with ID {book_id}...")
     self.checkout_df = self.storage.load_from_file(filename)
     if book_id in self.checkout_df['book_id'].values:
        raise ValueError(f"Book ID {book_id} already exists issued.")
     
     new_book = pd.DataFrame([{
        'book_id': book_id,
        'title': title,
        'issued_date': issued_date,
        'return_date': return_date,
        'user_id': user_id
    }])
     
     
     self.checkout_df = pd.concat([self.checkout_df, new_book], ignore_index=True)
     print(f"Book '{title}' added successfully.")
     storage.save_to_file(self.checkout_df,filename)



    def update_checkouts(self, filename, book_id, field,new_value,id):
        
     #Update a single field for a specific book and save the changes.
    # Check if the book exists
    
     logger.info(f"Updating book ID {book_id}...")
     user_id=id
     self.checkout_df = self.storage.load_from_file(filename)
     if book_id in self.checkout_df['book_id'].values:
         
        # Update the field if it exists in the DataFrame
        if field in self.checkout_df.columns:
            self.checkout_df.loc[self.checkout_df['book_id'] == book_id, field] = new_value
            print(f"Book ID {book_id} updated: {field} = {new_value}.")
        else:
            print(f"Field '{field}' not found.")
     else:
        print(f"Book with ID {book_id} not found.")


     logger.info("Saving updated DataFrame to file...")
     self.storage.save_to_file(self.checkout_df, filename)

    
    
    
 

    def delete_checkouts(self, book_id, filename):
     #Delete a book from the DataFrame and save the updated DataFrame to the file.
    
    # Load the DataFrame from the file
     logger.info(f"Deleting book ID {book_id}...")
     self.checkout_df = self.storage.load_from_file(filename)

    #Checking if it already exists
     if 'book_id' in self.checkout_df.columns and book_id in self.checkout_df['book_id'].values:
         

        df = self.checkout_df[self.checkout_df['book_id'] != book_id]
        print(f"Book ID {book_id} deleted successfully.")
     else:
        print(f"Book with ID {book_id} not found.")


     storage.save_to_file(df, filename)
     print("Updated DataFrame saved to file.")

      


    # def list_books(self):
    #     """List all available books."""
    #     if self.books_df.empty:
    #         print("No books available.")
    #     else:
    #         print(self.books_df)

    def save_checkouts(self, filename):
        #Save the books DataFrame to a file
        
        logger.info(f"Saving books to {filename}...")
        self.storage.save_to_file(self.checkout_df, filename)
        print(f"Books saved to {filename}.")
