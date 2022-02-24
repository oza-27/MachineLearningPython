# Develop a single python script which performs the following tasks:
# 1. Load the dataset titled RAILWAY and display all the available data fetched from the file [10 marks]
# 2. Display all the records where a train is travelling on both Monday and Wednesday [15 marks]
# 3. Display all the records where a train is travelling on Friday and also display the day name for Monday and Friday in all capital [15 marks]
# 4. Store the details of all such trains which are not running on Sunday to a new file titled as NotOnSunday.CSV [10 maks]
import csv

import pandas as pd
print("---------------------------1------------------------")
# 1. Load the dataset titled RAILWAY and display all the available data fetched from the file [10 marks]
url = "railway.csv"
data_frame = pd.read_csv(url)
print(data_frame.head(5))

print("--------------------------2---------------------------")

# 2. Display all the records where a train is travelling on both Monday and Wednesday [15 marks]
list1 = []
for i in data_frame["run_days"]:
    if "M" and "W" in i:
        list1.append(data_frame[data_frame["run_days"] == i])
print(list1)

print("---------------------------3--------------------------")
# 3. Display all the records where a train is travelling on Friday and also display the day name for Monday and Friday in all capital [15 marks]
list2 = []
for j in data_frame["run_days"]:
    if "M" and "F" in j:
        list2.append(data_frame[data_frame["run_days"] == j])
print(list2)

list3 = []
for k in data_frame["run_days"]:
    if "M" and "F" in k:
        if k[0] == "M":
            k = "Monday"
            print(k.upper())
print("----------------------------4---------------------------")

# 4. Store the details of all such trains which are not running on Sunday to a new file titled as NotOnSunday.CSV [10 maks]
list4 = []
for l in data_frame["run_days"]:
    if "S" not in l:
        list4.append(data_frame[data_frame["run_days"] == l])
print(list4)

with open("NotOnSunday.csv", "a") as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(list4)

print("--------------------------THE END-------------------------")
