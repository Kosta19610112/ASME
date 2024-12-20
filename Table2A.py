import os
import pandas as pd

# Path to the directory containing the files
directory_path = r"c:\Users\ksree\Documents\Git\ASME\Tablicy"

# List to store dataframes
dataframes = []

# Iterate through files in the directory
for file_name in sorted(os.listdir(directory_path)):
    if file_name.startswith("tablica2A"):
        print(f"Processing file: {file_name}")
        file_path = os.path.join(directory_path, file_name)
        
        # Read the file with error handling for encoding
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1', errors='replace') as file:
                lines = file.readlines()
        
        # Extract header from the first file and transform it
        if not dataframes:  # Check if this is the first file being processed
            header = lines[0].strip().split()  # Split by whitespace
            df = pd.DataFrame(columns=header)
        
        # Add rows to the dataframe
        for line in lines[1:]:
            row = line.strip().split()
            if len(row) == len(header):  # Check if the row matches the header length
                df.loc[len(df)] = row
            else:
                print(f"Skipping mismatched row in file {file_name}: {row}")
        
        # Append the dataframe
        dataframes.append(df)

# Combine all dataframes into one final dataframe
final_dataframe = pd.concat(dataframes, ignore_index=True)

# Display the final dataframe
print(final_dataframe)
