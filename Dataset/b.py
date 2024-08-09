import os
import pandas as pd

def extract_text_column(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            # Construct full file paths
            input_filepath = os.path.join(input_folder, filename)
            output_filepath = os.path.join(output_folder, filename)
            
            # Read the CSV file
            df = pd.read_csv(input_filepath)
            
            # Check if the "text" column exists
            if 'Tweets' in df.columns:
                # Extract the "text" column
                text_df = df[['Tweets']]
                
                # Save the new CSV with the same name in the output folder
                text_df.to_csv(output_filepath, index=False)
                print(f"Processed {filename}")
            else:
                print(f"No 'text' column in {filename}")

# Define the input and output folders
input_folder = '/Users/amitsharma/SummerSem/CourseWork/LLM/Project/Dataset'
output_folder = '/Users/amitsharma/SummerSem/CourseWork/LLM/Project/Dataset/Datset2'

# Run the extraction process
extract_text_column(input_folder, output_folder)
