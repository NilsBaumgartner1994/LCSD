import csv

def compare_csv_files(file1, file2):
    print("Create a dictionary with the values of the first file");
    # Create a dictionary with the values of the first file
    file2_data = {}
    title = ""

    with open(file2, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        title = headers[0]
        headers = next(reader)
        indexFileName = headers.index("FileName")
        indexDataClumps= headers.index("DataClumps")
        for row in reader:
            fileName = row[indexFileName]
            dataClumpValue = row[indexDataClumps]
            file2_data[fileName] = dataClumpValue

    print("Create a list with the rows of the second file where DataClumps is not 1")
    # Create a list with the rows of the second file where DataClumps is not 1
    result = []
    with open(file1, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        print(headers)
        indexFileName = headers.index("FileName")
        indexDataClumps= headers.index("DataClumps")
        for row in reader:
            fileName = row[indexFileName]
            dataClumpValue = row[indexDataClumps]
            if dataClumpValue != '' and dataClumpValue != "0":
                if fileName not in file2_data:
                    print(fileName+" not found data_clumps")
                    result.append(row)
#            if row[indexFileName] not in file1_data or file1_data[row['FileName']] != '1':
 #               result.append(row)

    # Save the result to a new file
    with open('diffWhatOurToolDontFound.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title,"","",""])
        writer.writerow(['ID', 'FileName', 'Package', 'DataClumps'])
        writer.writerows(result)


compare_csv_files('/Users/nbaumgartner/Desktop/ArgoUML-101_dataclumps.csv', '/Users/nbaumgartner/Desktop/lcsd.csv')
