# CsvColumnFilter ( Unique and Repeated Count)

<h3>Description</h3>

This Python script reads data from multiple CSV files, selects specific columns, copies unique data from those columns, writes it to a new CSV file, and adds the count of each value in front of the column. The script is useful for analyzing data stored in multiple CSV files and consolidating the unique values in selected columns.

<h3>Usage</h3>

To use this script, you should have Python 3 installed on your system. You can then download the script and run it from the command line using the following command:
```sh
python unique_csv_data.py
```

Before running the script, you need to specify the directory containing the CSV files and the columns to select in a dictionary called files_and_columns within the script. For example:

```sh
directory = "path/to/directory"
files_and_columns = {
    "file1.csv": ["column1", "column2"],
    "file2.csv": ["column3", "column4"],
    "file3.csv": ["column5", "column6"],
}
```

This dictionary specifies that the script should look for CSV files in the directory path/to/directory and select the columns column1 and column2 from file1.csv, the columns column3 and column4 from file2.csv, and the columns column5 and column6 from file3.csv. You can customize this dictionary to select the columns and files that you want to analyze.

After running the script, it will create a new CSV file called output.csv in the same directory as the input files. This file will contain the unique data from the selected columns, with the count of each value in front of the column name.

<h3>License</h3>

This script is licensed under the MIT License. You are free to use, modify, and distribute this script for any purpose, with or without attribution.



