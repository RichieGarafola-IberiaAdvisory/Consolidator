import streamlit as st
import pandas as pd
import os
import glob
from datetime import datetime
from pathlib import Path

# Streamlit configuration
st.set_page_config(page_title="Data Consolidation App", page_icon="📊")

# Set default directories
default_input_dir = Path.cwd() / 'Input'
default_output_dir = Path.cwd() / 'Output'

# Get list of folders in the current directory
folders = [str(path) for path in Path('.').rglob('*') if path.is_dir()]

# Select Input and Output Folders
input_dir = st.sidebar.selectbox('Select Input Folder:', folders, index=folders.index(str(default_input_dir)) if str(default_input_dir) in folders else 0, format_func=lambda x: Path(x).name)
output_dir = st.sidebar.selectbox('Select Output Folder:', folders, index=folders.index(str(default_output_dir)) if str(default_output_dir) in folders else 0, format_func=lambda x: Path(x).name)

# Manual input option for folders
input_dir_manual = st.sidebar.text_input('Input Folder (Manual):', str(default_input_dir))
output_dir_manual = st.sidebar.text_input('Output Folder (Manual):', str(default_output_dir))

# Use manual input if provided
input_dir = Path(input_dir_manual) if input_dir_manual else Path(input_dir)
output_dir = Path(output_dir_manual) if output_dir_manual else Path(output_dir)

# User input for sheet name, rows to skip, and output file name
st.header("Data Configuration")
with st.container():
    sheet_name = st.text_input("Sheet Name:", "Sheet1")
    rows_to_skip = st.number_input("Rows to Skip:", value=0)
    output_file_name = st.text_input("Output File Name:", "Consolidated_Input_Files")

# Get today's date
today = datetime.today().strftime('%d %b %Y')



# Display info about selected folders
with st.sidebar.expander("Selected Folders"):
    st.info(f"Selected Input Folder: {input_dir}")
    st.info(f"Selected Output Folder: {output_dir}")


# Display data processing and export in a clean layout
with st.expander("Data Processing"):
    # Consolidate and Export Data
    files = glob.glob(os.path.join(input_dir, "*.xlsx"))
    warnings_shown = False
    data_frames = []

    for f in files:
        try:
            temp_df = pd.read_excel(f, sheet_name=sheet_name, skiprows=rows_to_skip)
            temp_df['Source'] = Path(f).name
            data_frames.append(temp_df)
            st.success(f"File Imported: {f.split('/')[-1]}")
        except ValueError:
            if not warnings_shown:
                st.warning("Some files may have a different structure or sheet name. Check logs for details.")
                warnings_shown = True
            st.warning(f"Sheet '{sheet_name}' not found in {f.split('/')[-1]}. Skipping this file.")
        except Exception as e:
            st.error(f"Error reading {f.split('/')[-1]}: {e}")

if data_frames:
    df = pd.concat(data_frames)
    # Export the Consolidated Data to Excel
    if st.button('Export Consolidated Data to Excel'):
        output_file_path = output_dir / f'{output_file_name}.xlsx'
        df.to_excel(output_file_path, index=False)
        st.success(f"Consolidated data exported to: {output_file_path}")

    # Display Consolidated Data Preview
    st.subheader("Consolidated Data Preview")
    st.dataframe(df)
else:
    st.warning("No data frames were successfully read.")
