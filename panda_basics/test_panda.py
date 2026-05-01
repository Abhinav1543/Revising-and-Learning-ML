import pandas as pd

data = {
    "Name" : ["Abhinav","Arya","Aryan","Ashwani","Akasht","Anmol","Sarika","Deep"],
    "Age" : [1,3,42,51,66,100,1000,11],
    "Marks" : [22,33,44,55,66,100,10,1] 
}

df = pd.DataFrame(data)
# print(df)

# print(df.head())
# print(df.tail())
print(df.describe())
print(df.info())

