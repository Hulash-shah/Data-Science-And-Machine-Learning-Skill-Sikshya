import pandas as pd 

titanic_df = pd.read_csv(
    r"C:\Users\shahh\OneDrive\Desktop\Data Science And Machine Learning\Skill_Sikshya\Day22\titanic_data.csv",
    delimiter = ",",
    header = 0
    )

print(titanic_df)


# Conditional based Filtering

mask = titanic_df.Fare > 100

fare_100 = titanic_df[mask]
print(fare_100)
print(fare_100.shape)

print("Out of 891 passengers, only 53 passengers paid more than 100 in fare")


female_fare_100 = fare_100[fare_100.Sex == "female"]

print(female_fare_100.shape)


higher_class = titanic_df[titanic_df["Pclass"] == 1]

survived = higher_class[higher_class["Survived"] == 1]

survival_rate = len(survived) / len(higher_class) * 100


print(higher_class.shape)
print(survived.shape)
print(f"The survival rate of Higher-Class passenger is : {survival_rate :.2f}%")