import pandas as pd
import json


#Function: prepare_json_file
#Purpose: Preprocess the input json file so it can be loaded to
# pandas dataframe

def prepare_json_file(source_file_name, destination_file_name):

    #Declare empty list
    processed_lines = []
    
    # Open the source file in read mode
    with open(source_file_name, 'r') as source_file:

        #Add the list bracket to the beginning of the file
        processed_lines.append('[\n')
        
        # Check the record numbers
        line_count = sum(1 for _ in source_file)
        # Set the file pointer to the beginning of the file
        source_file.seek(0)
        row_number = 0

        for line in source_file:
            # Process the line as we need to skip the last line
            if row_number < line_count-1:
                processed_line = line.replace('}','},')  # Add comma at the end of each line
            else:
                processed_line = line

            processed_lines.append(processed_line)
            row_number = row_number +1 
        
        processed_lines.append(']')
    #  Create a new file and write the processed data
    with open(destination_file_name, 'w') as output_file:
        for processed_line in processed_lines:
            output_file.write(processed_line)

#Function: load_json_file_to_pandas_df
#Purpose: Preprocess the input json file so it can be loaded to
# pandas dataframe

def load_json_file_to_pandas_df(json_file_path):
    
    try:
        json_df = pd.read_json(json_file_path)
    except ValueError as e:
        print(f"Error: {e}")
        exit(0)


    return json_df

#Function: load_csv_file_to_pandas_df
#Purpose: Preprocess the input csv file so it can be loaded to
# pandas dataframe

def load_csv_file_to_pandas_df(csv_file_path):
    
    # Read the CSV file into a Pandas DataFrame
    encode_df = pd.read_csv(csv_file_path)
    
    # Create a bitlink column
    encode_df['bitlink'] = 'http://' + encode_df['domain'] +  '/' + encode_df['hash']
    return encode_df

#Function: process_data
#Purpose: This is the main functions and it is process the data
# The following steps are executed
# 1. Filter the decode_df to contain only the data for 2021
# 2. Join decode_df and encode_df dataframse by the bitlink
# 3. Group the data by the long_url from encode_df and count results
# 4. Sort the returned result by count descending
# The returned result is a data frame with 2 columns long_link, count

def process_data(decode_df,encode_df):
    
    # 1. Filter the decode_df to contain only the data for 2021
    filtered_df = decode_df[decode_df['timestamp'].between('2021-01-01', '2021-12-31')]
 
    # 2. Join decode_df and encode_df dataframse by the bitlink
    merged_df = pd.merge(filtered_df, encode_df, on='bitlink')

    # 3. Group the data by the long_url from encode_df and count results
    group_df = merged_df.groupby(['long_url'])['long_url'].count().reset_index(name='count')

    #4. Sort the returned result by count descending
    return group_df.sort_values(by='count', ascending=False)

#Function: prepare_output
#Purpose: Get the processed dataframe and prepare the json output.
#The requested output is in the following format  [{"LONG_URL": count}, {"LONG_URL": count}]
# This requieres the following preprocessing:
# The dataframe is exported to a dictionary containing the required format


def prepare_output(process_df,result_file_path):
    
    out_result = {}
    # Prepare the output dataframe 
    for index, row  in process_df.iterrows():
        out_result[row['long_url']] = row['count'] 

    # Open the file in write mode and write each key-value pair
    row_number = 0
    with open(result_file_path, 'w') as output_file:
        output_file.write('[\n')
        for key, value in out_result.items():
            if row_number > 0:
                output_file.write(',')
            json.dump({key: value}, output_file)
            row_number = 1
        output_file.write(']')           

# Functions
def main():
    
    #Declare the file names fariables
    source_json_file = 'decodes.json'
    preprocessed_json_file ='decodes_preprocessed.json'
    source_csv_file = 'encodes.csv'
    result_file_path = 'result.json'
   
    # Preprocess the json file
    print('Preprocess the json file')
    prepare_json_file(source_json_file,preprocessed_json_file)

    # Load the json file to pandas dataframe
    print('Load the json file to pandas dataframe')
    decode_df = load_json_file_to_pandas_df(preprocessed_json_file)

    # Load and preprocess csv dataframe
    print('Load and preprocess csv dataframe')
    encode_df = load_csv_file_to_pandas_df(source_csv_file)

    # Process the data
    print('Process the data')
    processed_df = process_data(decode_df,encode_df)

    # Post process Dump the file to result json
    print('Post process Dump the file to result json')
    prepare_output(processed_df,result_file_path)

# Conditional code to run the script only if it is the main module
if __name__ == "__main__":
    main()
