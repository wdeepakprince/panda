# importing packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# loading dataset
data=pd.read_excel("Holidays.xlsx")

#print 1st 5 rows
print("Head : 1st 5 rows :")
print(data.head())
print("\n")

#print full data
print("Complete Data :")
print(data)
print("\n")
