import pandas as pd
import os

class Storage:
    def __init__(self, directory="data"):
        
        
        #Initialize the storage with a directory for storing files.
        
        
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def load_from_file(self, filename):
        
        
        #Load data from either a JSON or CSV file and return as a DataFrame.
        filepath = os.path.join(self.directory, filename)

        if not os.path.exists(filepath):
            print(f"File {filename} not found.")
            return pd.DataFrame()  # Return an empty DataFrame if file not found

        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension == ".json":
            return self._load_from_json(filepath)
        elif file_extension == ".csv":
            return self._load_from_csv(filepath)
        else:
            print("Unsupported file format.")
            return pd.DataFrame()  # Return an empty DataFrame for unsupported format



    def _load_from_json(self, filepath):
        """Load data from a JSON file and return as a DataFrame."""
        try:
            return pd.read_json(filepath)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error

    def _load_from_csv(self, filepath):
        """Load data from a CSV file and return as a DataFrame."""
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error
    
    
    
    
    def save_to_file(self, df, filename):
        #Save a DataFrame to the specified CSV or JSON
        
        os.makedirs(self.directory, exist_ok=True)

        filepath = os.path.join(self.directory, filename)

        # Check if the file format is CSV or JSON
        
        if filename.endswith('.csv'):
            df.to_csv(filepath, index=False)
            print(f"Data saved to {filepath} (CSV format).")
        elif filename.endswith('.json'):
            df.to_json(filepath, orient='records', lines=True)
            print(f"Data saved to {filepath} (JSON format).")
        else:
            print("Unsupported file format. Please use .csv or .json.")