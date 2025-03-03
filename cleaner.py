def filter_airports(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split(':')
            if len(parts) > 4 and parts[4] == 'USA':
                outfile.write(line)

# Usage
filter_airports('GlobalAirportDatabase.txt', 'FilteredGlobalAirportDatabase.txt')
