import sqlite3
import pandas as pd

def excel_to_sqlite(excel_files_and_tables, db_file_path):
    """
    Convert multiple Excel files to a single SQLite database.

    :param excel_files_and_tables: List of tuples where each tuple is (excel_file_path, table_name).
    :param db_file_path: Path to the SQLite database file.
    """
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_file_path)
    
    for excel_file_path, table_name in excel_files_and_tables:
        # Load the Excel file
        excel_data = pd.read_excel(excel_file_path, sheet_name=None)  # Load all sheets
        
        for sheet_name, df in excel_data.items():
            # Create a full table name using the file's table_name and the sheet name
            full_table_name = f"{table_name}_{sheet_name}"
            
            # Write each sheet into the SQLite database as a table
            df.to_sql(full_table_name, conn, if_exists='replace', index=False)
            print(f"Stored {sheet_name} from {excel_file_path} as {full_table_name} in the DB.")
    
    conn.close()
    print(f"All Excel files have been converted to {db_file_path} SQLite database.")

# Example usage:
excel_files_and_tables = [
]

while True:
    add_table = input("insert Y/y to add table. Press 'Enter' to exit:")
    if add_table == "":
        break
    file_path = input("insert file path: ")
    table_name = input("insert table name: ")
    excel_files_and_tables.append((file_path, table_name))

db_file_path = input("Insert DB file path. File created if not already exists: ")  # Path to the output SQLite database
excel_to_sqlite(excel_files_and_tables, db_file_path)