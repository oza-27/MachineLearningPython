# import pandas as pd
#
# url = 'Titanic.csv'
#
# data_frame = pd.read_csv(url)
#
# Display the first few records (first 5 records)
# print(data_frame.head(5))
#
# print("--------------------------------------------------------- --------------------------")
#
# dimension of the data set
# print(data_frame.shape)
#
# print("-----------------------------------------------------------------------------------")
#
# Display standard statistics from the data
# print(data_frame.describe())
#
# print("-----------------------------------------------------------------------------------")
#
# Display the first record
# print(data_frame.head(1))
# print(data_frame.iloc[0])
# print(data_frame.iloc[:4])
#
# print("-----------------------------------------------------------------------------------")
#
# Print all details where passengers class is '2'
# print(data_frame[data_frame['Pclass'] == 2].head(1))
#
# print("-----------------------------------------------------------------------------------")
#
# Print details of male passengers from class 2
# print(data_frame[(data_frame['Pclass'] == 2) & (data_frame['Sex'] == 'male')])
#
# print("-----------------------------------------------------------------------------------")
#
# replace the values to some other meaningful content/description
# replace all 'male' as 'men' and 'female' as 'women'
# print(data_frame['Sex'].replace(["male", "female"], ["Men", "Women"]))
#
# print("-----------------------------------------------------------------------------------")
#
# Print all travelling class of passengers in human readable format
# i.e 1: First
# i.e 2: Second
# print(data_frame['Pclass'].replace([1, 2, 3], ["First", "Second", "Third"]))
#
# print("----------------------------------------------------------------------------------")
#
# Rename some columns names to desired names
# print(data_frame.rename(columns={'Pclass': 'Passenger Class', 'Sex': 'Gender'}).iloc[0])
#
# print("---------------------------------------------------------------------------------")
#
# Print the min, max, count, sum, mean fare of the trip
# print('Max fare collected: ', data_frame['Fare'].max())
# print('Min fare collected: ', data_frame['Fare'].min())
# print('Count of fare collected: ', data_frame['Fare'].count())
# print('Sum of fare: ', data_frame['Fare'].sum())
# print('Mean of Fare column: ', data_frame['Fare'].mean())
#
# print("---------------------------------------------------------------------------")
#
# Create the new data frame having only columns that are required for further calculation
# print(data_frame.drop('Age', axis=1).iloc[0])
#
# print("-------------------------------------------------------------------------")
#
# Creating new data frame and then drop columns and rename the collumn name
# data_frame_work = data_frame.drop(['SibSp', 'Parch', 'Ticket', 'Cabin'], axis=1)
# data_frame_work = data_frame_work.rename(columns={'Pclass': 'Passenger Class', 'Sex': 'Gender'})
#
#
# print(data_frame_work.iloc[0])
#
# print("------------------------------------------------------------------------")
#
# Print unique passenger class from the data set
# print(data_frame_work['Passenger Class'].unique())
#
# print("------------------------------------------------------------------------")
#
# print the total passengers travelling in each class
# print(data_frame_work['Passenger Class'].value_counts())
#
# print("------------------------------------------------------------------------")
#
# Work with missing values
# Display all such records where age is not specified
# print(data_frame_work['Age'].isnull())
# print(data_frame_work.shape)
#
# print("-------------------------------------------------------------------------")
#
# Remove duplicats from data frame
# print(data_frame_work.drop_duplicates())
# print(data_frame_work.drop_duplicates(subset=['Gender']))
#
# print("-------------------------------------------------------------------------")
#
# Show the mean age of each gender
# print(data_frame_work.groupby('Gender').mean())
#
# print("---------------------------------------------------------------------------")
#
# Show count of pasengers embarked as per gender
# print(data_frame_work.groupby(['Gender', 'Embarked'])['Age'].count())
#
# print("---------------------------------------------------------------------------")
# Print all names in upper case
# print(data_frame_work['Name'])
# for name in data_frame_work:
# print(name.upper())
# print([name.upper() for name in data_frame_work['Name']])
#
#
# def upper_case(name=''):
#     return name.upper()
#
#
# print(data_frame_work['Name'].apply(upper_case))
# print(data_frame_work.groupby('Gender').apply(lambda value: value.count()))
#
# Concat and meger datasets