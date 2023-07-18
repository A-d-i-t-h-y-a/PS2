import os
import sys

# Define the input files and output file path
input_files = [os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])]
output_file = f'{os.getcwd()}/gmw_nellore_{sys.argv[1][-11:-7]}.tif'

# Create the input file list text
input_list_text = '\n'.join(input_files)

# Define the temporary input file path
temp_input_file = f'{os.getcwd()}/temp_input_files.txt'

# Write the input file list to the temporary file
with open(temp_input_file, 'w') as file:
    file.write(input_list_text)

# Define the command
command = f'gdal_merge.py -pct -n 0.0 -a_nodata 0.0 -ot Byte -of GTiff -o "{output_file}" --optfile "{temp_input_file}"'
# gdal_merge.py -pct -n 0.0 -a_nodata 0.0 -ot Byte -of GTiff -o "/home/adithya/Project School/gmw/abcd.tif" --optfile /tmp/processing_xLqsPO/555a130cd1c7494f8db073be84b2d643/mergeInputFiles.txt

# Execute the command
os.system(command)

# Remove the temporary input file
# os.remove(temp_input_file)

