"""module for mushroom project"""
# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and read csv file
df = pd.read_csv("mushroom_data.csv")
# print mushroom data - head to see 10 row of the data
#print(mushroom_data)


# list of all column headers
for index in range(0, len(df['Bruises'])):
    df['Bruises'][index] = str(df['Bruises'][index])
columns = df.columns.tolist()

# loop through all the columns in the coulmns list and print columns
# Sns countplot to show the columns from the data
for column in columns:
    sns.countplot(x=df[column], data=df, order=df[column].value_counts())
    plt.xticks(rotation=30, fontsize=10)
    plt.xlabel(column, fontsize=12)
    plt.title(column + " Value Counts")
    #print(columns)
    plt.show()
    plt.clf()

"""This is not production ready code at this time"""