def reformat_qubit_file(input_file, output_file, line_length=30):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        binary_data = infile.read().replace('\n', '')  # Read all data and remove newlines
        for i in range(0, len(binary_data), line_length):
            outfile.write(binary_data[i:i + line_length] + '\n')  # Write fixed-length lines

# Example usage
reformat_qubit_file('qubit.txt', 'reformatted_data.pi')
