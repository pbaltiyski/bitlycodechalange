# bitlycodechalange

# Overview

This Python script is designed to read the source data , load them into Pandas DataFrames, perform data processing (grouping and aggregating), and generate a JSON output. The script is structured with several functions to achieve specific tasks.

# Design overview

## Source data
* encode.csv: the act of shortening a long link into a bitlink on the Bitly platform.
* decode.json: a metric collected each time a bitlink is accessed and performs the redirect. The data in the file provided is not very well structured. This is the reason why it required preprocessing

## Process design

### Overview
Pandas library is chosen because of the ease of processing and executing SQL like operations on data.

### Preprocess decode json
As mentioned above the file is not following the json standards. Because of it the following is required:
* Add '[' in the beginning and ']' at the end of the script
* Add a comma at the end of each {} block 

### Load the process json in pandas dataframe
Load the data in to pandas dataframe

### Load and preprocess the encode
The process is loading the CSV file and generating the bitlink

### Process data
The following operations are executed:
* Filter the decodes for only year 2021
* Join the encodes and decodes based on bitlink
* Group and count the records by longlinc

### Export the data in json format
The steps export the dataframe to dictionary and dump the data to result.json file.



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

### Unittest

The unittests are created in the file test_bcc.py. They should be invoked by the script below

```bash
python -m unittest test_bcc.py
```

### File Structure
<strong>decodes.json</strong>: Input JSON file.

<strong>decodes_preprocessed.json</strong>: Output of the preprocessing step.

<strong>encodes.csv</strong>: Input CSV file.

<strong>result.json</strong>: Final processed output.

The result files are uploaded for clarity.

### Dependencies

pandas
unittest


# Notes

Ensure that the input files (decodes.json and encodes.csv) are present in the script's directory.
