import sys
import csv
import xml.etree.ElementTree as ET

filename_map = {}

file = sys.argv[1]
tree = ET.parse(file)
root = tree.getroot()

for problem in root:
    file_tag = problem.find("file")
    #filename = file_tag.text.split("/")[-1]
    filename = file_tag.text
    filename = filename.replace("file://$PROJECT_DIR$", "src")
    #print("Filename: "+filename)
    filename_map[filename] = filename_map.get(filename, 0) + 1

unique_filenames_len = len(filename_map.keys())
unique_filenames = sorted(list(set(filename_map.keys())))

print("Unique filenames:")
for filename in unique_filenames:
    print(filename)
print("Number of unique filenames:", unique_filenames_len)
