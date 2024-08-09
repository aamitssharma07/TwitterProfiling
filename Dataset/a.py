import os
import pandas as pd

def extract_content_column(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the specified folder
    for filename in os.listdir(input_folder):
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            
            # Read the CSV file
            try:
                df = pd.read_csv(file_path)
                # Check if 'content' column exists
                if 'content' in df.columns:
                    # Extract the 'content' column
                    content_column = df[['text']]
                    
                    # Save the 'content' column to a new CSV file in the output folder
                    content_file_path = os.path.join(output_folder, filename)
                    content_column.to_csv(content_file_path, index=False)
                    print(f"Saved content column to {content_file_path}")
                else:
                    print(f"'content' column not found in {filename}")
            except Exception as e:
                print(f"Error reading {filename}: {e}")

# Specify the input and output folder paths
input_folder = '/Users/amitsharma/SummerSem/CourseWork/LLM/Project/Dataset'
output_folder = '/Users/amitsharma/SummerSem/CourseWork/LLM/Project/Dataset/Datset2'

# Run the function
extract_content_column(input_folder, output_folder)
