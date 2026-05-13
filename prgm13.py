import os.path
import sys

fname = input("Enter the filename to sort: ")

# Check whether file exists
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

# Read file contents
infile = open(fname, "r")
lines = infile.readlines()
infile.close()

linelist = []

# Remove newline characters
for line in lines:
    linelist.append(line.strip())

# Sort lines
linelist.sort()

# Create output file
outfile = open("sorted.txt", "w")

# Write sorted lines
for line in linelist:
    outfile.write(line + "\n")

outfile.close()

print("sorted.txt contains", len(linelist), "lines")