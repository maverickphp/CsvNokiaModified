import csv
import os

# specify the directory containing the CSV files and the columns to select
directory = "path/to/directory"
files_and_columns = {
    "file1.csv": ["column1", "column2"],
    "file2.csv": ["column3", "column4"],
    "file3.csv": ["column5", "column6"],
}

# create a dictionary to hold the unique data for each column and its count
unique_data = {}
for columns in files_and_columns.values():
    for column in columns:
        unique_data[column] = {}

# read from the CSV files and select the columns
for file, columns in files_and_columns.items():
    file_path = os.path.join(directory, file)
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for column in columns:
                value = row[column]
                if value not in unique_data[column]:
                    unique_data[column][value] = 1
                else:
                    unique_data[column][value] += 1

# write the unique data and its count to a new CSV file
output_path = os.path.join(directory, "output.csv")
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    header = []
    for column in unique_data.keys():
        header.append(column)
        header.append("count")
    writer.writerow(header)
    for value in set.union(*[set(d.keys()) for d in unique_data.values()]):
        row = []
        for column, data in unique_data.items():
            if value in data:
                row.append(value)
                row.append(data[value])
            else:
                row.append("")
                row.append("")
        writer.writerow(row)
