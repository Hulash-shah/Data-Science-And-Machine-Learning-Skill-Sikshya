import pandas as pd

# Datatype of Pandas

# 1. DataFrame -> 2D Table with rows and columns

# 2. Series -> 1D array-like, can hold any type of data type such as int, str , float , python objects


# Creating DataFrame

data = {
    "name" : ["Bob", "Aman", "Hulash"],
    "age" : [24,25,24]
}

df = pd.DataFrame(data)
print(df)


titanic_df = pd.read_csv(
    r"C:\Users\shahh\OneDrive\Desktop\Data Science And Machine Learning\Skill_Sikshya\Day22\titanic_data.csv",
    delimiter = ",",
    header = 0
    )

print(titanic_df)
print(titanic_df.shape)

# json_df = pd.read_json("user.json")

# Sneak Peak
print(titanic_df.head(6))


# Reading a column

name = titanic_df["Name"]
print(name)

print(type(name))

name_age = titanic_df[["Name", "Age"]]

print(name_age)

# Reading Rows
row1 = titanic_df["Name"]

print(row1)

row = titanic_df.loc[2]

print(row)

print(titanic_df.dtypes)

print(titanic_df.info())