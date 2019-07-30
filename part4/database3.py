import csv

file = "D:\\dataset\\datacamp\\introduction to databases in python\\Census.csv"
data = open(file, 'r')
csv_reader = csv.reader(data)
for row in csv_reader:
    print(row)

