import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"
df = pd.read_csv(url)
n=7
print(df.head()) #prints first n rows, if not specified print first 5 rows
print(df.tail(n)) #prints last n rows, if not specified print last 5 rows
print(df.info()) #prints top 30 rows and botton 30 rows

print(df.dtypes) # prints datatypes
print(df.describe()) #returns statistical summary (count,mean,std,min,...,max). 
#By default this skips rows and columns that do not contain numbers.
print(df.default(include="all")) #this includes object datatypes as well. 


path = "C:\\Users\\MYBOOK\\Desktop\\python\\data analysis with python\\automobile.csv"
df.to_csv(path)  #preserves progress anytime by saving modified dataset 