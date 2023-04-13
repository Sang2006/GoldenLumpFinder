import sys
import os
import json
import base64
import binascii

def find_number(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
        # Remove characters after '%'
        content = content.split('%')[0]
        # Remove remaining '%'
        content = content.replace('%', '')
        # Add padding if it's missing
        content += '=' * (-len(content) % 4)
        try:
            decrypted_content = base64.b64decode(content.encode()).decode("utf-8")
        except binascii.Error:
            return None
        index = decrypted_content.find(";;")
        if index == -1:
            return None
        else:
            number = decrypted_content[index-1]
            if number == "2":
                return file_name
            else:
                return None

if __name__ == "__main__":
    # Get the path to the folder containing the save files
    folder_path = sys.argv[1]
    
    # Create an empty list to hold the file names where a golden lump is found
    golden_lumps = []
    
    # Iterate over each file in the folder and check for golden lumps
    for file_name in os.listdir(folder_path):
        full_file_path = os.path.join(folder_path, file_name)
        
        # Print the current file being scanned
        print("Scanning file:", full_file_path)
        
        # Check if the current file contains a golden lump
        if find_number(full_file_path):
            golden_lumps.append(file_name)
    
    # Write the list of file names with golden lumps to a JSON file
    with open("golden_lumps.json", "w") as f:
        json.dump(golden_lumps, f)
    
    # Print the list of file names with golden lumps
    print("Files with golden lumps:", golden_lumps)
