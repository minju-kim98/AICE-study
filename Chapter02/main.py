import numpy as np

a = np.array([1,2,3,4,5])
b = np.array(['대한민국', '포르투갈', '가나', '우루과이'])
c = np.array([1,2,'대한민국', '포르투갈'])

print(a)
print(b)
print(c)


print("------------------------------------------------------------------------------------")

import pandas as pd

s = pd.Series(['대한민국', '포르투갈', '가나', '우루과이'], index=['가', '나', '다', '라'], name="2022 카타르월드컵 H조")

print(s)

print("------------------------------------------------------------------------------------")

a1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
print(a1)
print()

a2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["a", "b", "c"])
print(a2)

print("------------------------------------------------------------------------------------")

flight = pd.read_csv('./Clean_Dataset.csv', encoding="cp949")
print(flight)

print("------------------------------------------------------------------------------------")

a2.to_csv("./result_a2.csv")

result = pd.read_csv("./result_a2.csv", encoding="cp949")
print(result)

print("------------------------------------------------------------------------------------")

flight2 = pd.read_csv('./Clean_Dataset.csv', index_col='stops', usecols=['stops', 'departure_time', 'arrival_time', 'destination_city'])
print(flight2)

print("------------------------------------------------------------------------------------")

pd.crosstab(index=flight.source_city, columns=flight.arrival_time)