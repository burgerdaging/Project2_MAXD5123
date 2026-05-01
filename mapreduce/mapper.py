"""
MAPPER: Reads each row from stdin and emits 
This is the 'tally shouter' — for every passenger, shout their class with a count of 1.
"""
import sys
import csv

# Use csv.reader to safely handle commas inside quoted names
reader = csv.reader(sys.stdin)

# Skip the header row
# header = next(reader, None)

for fields in reader:
    try:
        # Pclass is the 3rd column (index 2)
        pclass = fields[2].strip()
        
        # Output: key<TAB>value (Hadoop standard format)
        print(f"{pclass}\t1")
    except (IndexError, ValueError):
        # Skip any malformed rows gracefully
        continue