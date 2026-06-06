#pre-processsing converting or mapping data from one 'raw' form to another format to make it ready for further analysis.
# a.k.a data-cleaning or data wrangling
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"
df = pd.read_csv(url)
df["acceleration"]=df["acceleration"]+1 #adds 1 to the values in the column "accerlation"
print(df["acceleration"])

#dealing with missing values:

#drop the missing values
 #drop the variable
 #drop the data entry

#replace the missing values
 #replace with average
 #replace with frequency
 #replace it based on other functions

#leave it as misssing
df.dropna(subset=["acceleration"], axis=0) #does not modify the dataframe, but used to check if the operation is correct
df.dropna(subset=["acceleration"], axis=0, inplace=True) #Modifies the dataframe

mean=df["acceleration"].mean() #finds the mean of the column acceraltion
df["acceleration"].replace(np.nan, mean) #replaces missing values with mean.

df["mpg"]=235/df["mpg"] #formula applied to all values in column 'mpg'
df.rename(columns={"mpg":"L/100km"}, inplace=True) #changes the 'mpg' -> 'L/100km'

print(df["weight"].dtype) #print datatype of that column
df["weight"]=df["weight"].astype("float") #converts datatype
print(df["weight"].dtype)