# Define the required line length (including the leading space)
required_line_length = 28  # This is an example; adjust it as per your data.pi file

# Open the rdata.pi file for reading
with open('rdata.pi', 'r') as infile:
    rdata_lines = infile.readlines()

# Open a new file to save the corrected version
with open('rdata_corrected.pi', 'w') as outfile:
    for line in rdata_lines:
        # Strip any existing whitespace from the line
        line = line.strip()
        
        # If the line is too short, pad it with '0's; if it's too long, truncate it
        if len(line) < required_line_length - 1:  # Account for the space
            line = line.ljust(required_line_length - 1, '0')
        elif len(line) > required_line_length - 1:
            line = line[:required_line_length - 1]
        
        # Write the corrected line to the new file with a leading space
        outfile.write(f" {line}\n")

print("rdata.pi has been corrected and saved as rdata_corrected.pi.")
