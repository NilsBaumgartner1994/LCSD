import sys
import os
import csv
import xml.etree.ElementTree as ET

filename_map = {}

rootFolder = "/Users/nbaumgartner/Desktop/";

file_path = sys.argv[1]
rootFolder = base_path = os.path.dirname(file_path)
print("rootFolder: "+rootFolder);

tree = ET.parse(file_path)
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

# Save the sorted filenames to a CSV file
with open(rootFolder+"/"+'lcsd.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ArgoUML-0.26Beta-Unified 2", "", "", ""])
    writer.writerow(["ID", "FileName", "Package", "DataClumps"])
    for i, filename in enumerate(unique_filenames):
        writer.writerow([i, filename, "app", "1"])

print("Unique filenames:")
for filename in unique_filenames:
    print(filename)
print("Number of unique filenames:", unique_filenames_len)
