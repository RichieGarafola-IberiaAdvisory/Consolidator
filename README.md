# Data Consolidation Script

This Python script is designed to consolidate data from multiple Excel files located in the "Input" folder and export the consolidated data to an Excel file in the "Output" folder.

---

## Overview

**The script performs the following main tasks:**

- Consolidation of Data:
    - Reads data from multiple Excel files using Pandas.
    - Concatenates data frames and handles exceptions during file processing.

---

## Usage


### Install Dependencies:
Ensure that you have the required packages installed by running:
        
        pip install pandas streamlit
        
### Folder Structure:
Make sure to organize your Excel files in the "Input" folder within the same directory as the script. The consolidated output will be saved in the "Output" folder.

### Run the Script:
Execute the script in a Python environment. The consolidated data will be exported to a file named "Consolidated_Input_Files.xlsx" in the "Output" folder.

---

## Script Explanation

### Import Packages

- pandas: Data manipulation library.
- os: Operating system interaction.
- glob: File path pattern matching.
- warnings: Suppress warnings during Excel file reading.
- datetime: Obtain current date and time.
- streamlit: GUI application.


### Set Input / Output Folder Directories

- input_dir: Directory path for input Excel files.
- output_dir: Directory path for the output consolidated file.

### Data Consolidation

- Create file paths to be read in:
    - Glob function is used to get a list of Excel files in the "Input" folder.
    - Read data from multiple Excel files using Pandas.

<!-- --- -->

- Don't show Excel data validation warning:
    - Warnings related to Excel data validation are suppressed.

<!-- --- -->

- Store data frames:
    - An empty list (data_frames) is created to store individual data frames.

<!-- --- -->

- Loop through each file in the input folder:
    - For each Excel file, it reads the "Data" sheet and adds a new column "Source" to store the file name.
    - Successfully read data frames are stored in the dataframes list.
    - Messages are printed indicating successful file import or reasons for skipping.

<!-- --- -->

- Concatenate all successfully read data frames:
    - If there are any successfully read data frames, they are concatenated into a single data frame (df).

<!-- --- -->

- Export the Consolidated Data to Excel:
    - The consolidated dataframe is exported to an Excel file in the "Output" folder.

<!-- --- -->

- Consolidated Data Preview:
    - The consolidated data frame is printed for a quick preview.
    
---

## Notes

- If no dataframes are successfully read, a corresponding message will be printed.
- Ensure that the Excel sheets in the input files have a sheet named "Details" for successful reading.
- In case of errors during reading, error messages will be printed for troubleshooting.
- The 'Input' and 'Output' folders are created if they do not exist.

---
---

*Disclaimer: This script assumes a specific environment and configuration. Adjustments may be needed based on individual system setups and requirements.*
