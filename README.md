# Golden Lump Finder
The Golden Lump Finder is a Python program that searches a directory of cookie clicker save files for "golden lumps". A golden lump is identified by a specific marker within the file. The program reads each file, decodes any base64-encoded content, looks for the marker, and identifies files with golden lumps. It outputs the list of file names with golden lumps to a JSON file.

## Usage
### Exporting save files
I've also made an auto hotkey script for easy save exports. This is save you alot of time and effort. If you dont want to use the ahk file you can always do it manually.
You atleast want to have 600 save files because golden lumps are quite rare.
### Finding golden lumps
1. Download the golden_lump_finder.py file to your computer.
2. Open a command prompt or terminal window.
3. Navigate to the directory where the golden_lump_finder.py file is saved.
4. Type the following command to run the script: ```python3 golden_lump_finder.py path_to_directory```
5. Replace path_to_directory with the path to the directory containing the files you want to search.
6. Press Enter to run the command.

The program will then begin scanning the directory for files with golden lumps. As it scans each file, it will print out the name of the file it is currently processing. Once the program has finished scanning all the files, it will output a list of file names with golden lumps to a JSON file called golden_lumps.json in the same directory as the Python script.

## Contributions
Contributions to this project are welcome. Feel free to submit issues or pull requests if you encounter any problems or have ideas for improvements.
