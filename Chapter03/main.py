import pandas as pd
import numpy as np

flight = pd.read_csv("./Clean_Dataset.csv", encoding="cp949")
print(flight)
print(flight.head())
print(flight.tail())
print(flight.head(n=10))
print(flight.tail(n=3))

print("------------------------------------------------------------------------------------")

print(flight.shape)
print(flight.columns)
print(flight.info())
print(flight.describe())
print(flight.describe(include="all"))
print(flight.dtypes)
print(flight['source_city'].value_counts())