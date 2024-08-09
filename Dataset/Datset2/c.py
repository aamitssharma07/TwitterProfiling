import pandas as pd
import os

def remove_nan_rows_from_files(folder_path):
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing {file_path}")
            
            # Read the CSV file
            df = pd.read_csv(file_path)
            print(f"Original number of rows: {len(df)}")
            
            # Display the initial DataFrame for debugging
            print("Initial DataFrame:")
            print(df)
            
            # Replace 'nan', 'NaN', and '' strings with actual NaN values
            df.replace(['nan', 'NaN', ''], pd.NA, inplace=True)
            
            # Remove rows that contain only NaN values
            df.dropna(how='all', inplace=True)
            
            # Display the cleaned DataFrame for debugging
            print("Cleaned DataFrame:")
            print(df)
            
            print(f"Number of rows after removing NaN rows: {len(df)}")
            
            # Save the cleaned DataFrame back to the same file
            df.to_csv(file_path, index=False)

# Specify the path to the folder containing your CSV files
folder_path = '/Users/amitsharma/SummerSem/CourseWork/LLM/Project/Dataset/Datset2'

# Call the function to remove NaN rows from all CSV files in the folder
remove_nan_rows_from_files(folder_path)
