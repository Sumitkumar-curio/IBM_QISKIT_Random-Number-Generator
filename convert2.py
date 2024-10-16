# Correct the format of rdata.pi to match data.pi

# Define the required line length, including the leading space
required_line_length = 28  # 1 space + 27 bits

# Input and output file paths
input_file = 'rdata.pi'  # Your original rdata.pi file
output_file = 'correct_rdata.pi'  # The corrected output file

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Remove any extra spaces or newlines from the line
        line = line.strip()

        # Ensure the line is exactly 27 bits long (after the space)
        if len(line) < required_line_length - 1:
            # If the bitstring is too short, pad with '0's
            line = line.ljust(required_line_length - 1, '0')
        elif len(line) > required_line_length - 1:
            # If the bitstring is too long, truncate it
            line = line[:required_line_length - 1]

        # Write the corrected line with a leading space
        outfile.write(f" {line}\n")

print(f"Corrected file saved as {output_file}")
