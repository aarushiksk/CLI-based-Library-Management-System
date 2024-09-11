### For logging in as admin:
- id: 1
- password: 1234

### For logging in as a user
-id: 3
-password: 3456


## Folder structure is as follows:
1. data:
   - Contains Books.csv and Checkout.csv (can be used as database)
2. database:
   - Used sqlite3 for storing user and admin details securely

3. modules:
   - user_management: For managing users
   - book_management: For managing book related operations Eg: Adding, updating, deleting details
   - checkout_management: For storing issued books
  
4. utils:
   - Contains repeatedly used functions
     
5. dummy.py:
   - Use this for adding dummy values to user.db

6. main.py:
   - For running application using CLI
     
7. storage.py:
   - Takes in CSV and JSON files as well as saves them back to the local PC

### Data Flow diagram:

   <img width="653" alt="image" src="https://github.com/aarushiksk/CLI-based_Library-Management-System/Data Flow Diagram.jpeg](https://github.com/aarushiksk/CLI-based-Library-Management-System/blob/main/Data%20Flow%20Diagram.jpeg">
