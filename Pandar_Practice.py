import pandas as pd

url = "Titanic.csv"

data_frame = pd.read_csv(url)

# It will display few records of data frame
print(data_frame.head(10))

print("-----------------------------------")

# It will display the dimensions of data frame
print("Dimension of the data frame:)")
print(data_frame.shape)

print("------------------------------------")

# It will display the standard statistics of data frame
print("This are the standard statistics of the data frame")
print(data_frame.describe())

print("------------------------------------")

# It will display the first record
print("The first records are")
print(data_frame.head(1))
print(data_frame.iloc[0])
print("It shows record of the last 4 data from the data frame")
print(data_frame.iloc[:4])

print("-------------------------------------")

# It will display the records which has the Pclass = 3
print("The passengers having class 3 are:- ")
print(data_frame[data_frame["Pclass"] == 3].head(5))

print("-------------------------------------")

# Display the female passengers who is having Passenger class = 3
print("The female members who is having passengers class 3 are:- ")
print(data_frame[(data_frame["Pclass"] == 3) & (data_frame["Sex"] == "female")].head(5))

print("-------------------------------------")

# It replaces the values
print("Replaces values are:- ")
print(data_frame["Sex"].replace(["male", "female"], ["Choro", "Chori"]))

print("--------------------------------------")

# It displays the min, max, count, sum, mean fare of the trip
print("Minimum collected fare is:-", data_frame["Fare"].min())
print("Maximum collected fare is:-", data_frame["Fare"].max())
print("Count of total fare is:- ", data_frame["Fare"].count())
print("Sum of the trip is:- ", data_frame["Fare"].sum())
print("Mean of the fare column:- ", data_frame["Fare"].mean())

print("--------------------------------------")

# let's create the new data frame and then drop columns and rename the column name
print("This will drop the columns form the data frame")
new_data = data_frame.drop(["SibSp", "Parch", "Ticket", "Cabin"], axis=1)
print("This will rename the columns names from the data frame")
new_data = new_data.rename(columns={"Pclass": "Passenger Class", "Sex": "Gender"})
print(new_data.head(5))

print("---------------------------------------")

# Display the unique number of passenger class
print("The unique number of passenger class is:- ")
print(new_data["Passenger Class"].unique())

print("---------------------------------------")

# Display the value counts of passenger class
print("Total value counts of passenger class is:-")
print(new_data["Passenger Class"].value_counts())

print("---------------------------------------")

# Fill up missing values
print("This displays the missing values in specific columns:-")
print(new_data["Age"].isnull())
print(new_data.shape)

print("----------------------------------------")

# Removing duplicates from data frame
print("This will emove duplicates from data frame")
print(new_data.drop_duplicates())
print(new_data.drop_duplicates(subset=["Gender"]))

print("----------------------------------------")

# Showing the mean of each gender
print("This will show the mean of each gender")
print(new_data.groupby("Gender").mean())
print("This will show the count of passengers embarked as per gender:-")
print(new_data.groupby(["Gender", "Embarked"])["Age"].count())

print("----------------------------------------")

# Printing all the names in upper case
print(new_data["Name"])
for name in new_data:
    print(name.upper())
    print([name.upper() for name in new_data["Name"]])


def upper_case(name=''):
    return name.upper()


print(new_data["Name"].apply(upper_case))
print(new_data.groupby("Gender").apply(lambda value:value.count()))

print("------------------------------------------THE END---------------------------------------------------")
