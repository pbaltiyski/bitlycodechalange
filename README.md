# bitlycodechalange

# Overview

This Python script is designed to preprocess JSON and CSV files, load them into Pandas DataFrames, perform data processing, and generate a JSON output. The script is structured with several functions to achieve specific tasks.

# Script Structure

## 1. prepare_json_file
Purpose: Preprocess the input JSON file to prepare it for loading into a Pandas DataFrame.

Parameters:
source_file_name: Path to the source JSON file.
destination_file_name: Path to the destination preprocessed JSON file.
## 2. load_json_file_to_pandas_df
Purpose: Load a preprocessed JSON file into a Pandas DataFrame.

Parameters:
json_file_path: Path to the preprocessed JSON file.
## 3. load_csv_file_to_pandas_df
Purpose: Load and preprocess a CSV file into a Pandas DataFrame.

Parameters:
csv_file_path: Path to the source CSV file.
## 4. process_data
Purpose: Main function for processing data. It filters, joins, groups, and sorts data based on specific criteria.

Parameters:
decode_df: DataFrame containing decoded data.
encode_df: DataFrame containing encoded data.
## 5. prepare_output
Purpose: Prepare the output JSON file in a specific format.

Parameters:
process_df: Processed DataFrame.
result_file_path: Path to the output JSON file.
## 6. main
Purpose: Main entry point for the script. Calls functions in a sequence to execute the entire workflow.

## Usage

Ensure you have Python installed.
Install required dependencies by running:
```bash
make requirements
```

Run the script:
```bash
make
```

Check the result in the specified output files.
File Structure
### decodes.json: Input JSON file.

### decodes_preprocessed.json: Output of the preprocessing step.

### encodes.csv: Input CSV file.

### result.json: Final processed output.

### Dependencies

pandas

# Notes

Ensure that the input files (decodes.json and encodes.csv) are present in the script's directory.
