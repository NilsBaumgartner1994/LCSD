import csv
import sys

# Get the input file path from command line argument
input_file = sys.argv[1]

# Open the input file
with open(input_file, 'r') as file:
    reader = csv.reader(file)

    # Skip the first row
    next(reader)

    # Create a list to store the output rows
    output_rows = []

    # Loop over each row in the input file
    for row in reader:
        # Extract the relevant fields
        file_path = row[1]
        data_clumps = int(row[3])

        # Check if the data clumps value is greater than 0
        if data_clumps > 0:
            # Create a new row with the desired format
            output_row = [file_path, data_clumps]

            # Append the new row to the output rows list
            output_rows.append(output_row)

# Construct the output file name
output_file = input_file.split('.')[0] + '-comparable.csv'

# Open the output file and write the output rows
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FilePath', 'DataClumps'])
    writer.writerows(output_rows)

print(f"Output file saved as '{output_file}'")
