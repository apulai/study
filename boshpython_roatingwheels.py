import numpy as np
import pandas as pd

print("numpy and pandas demo")

print("Any function demo")
mylist = [False, True, False]
x = any(mylist)
print(mylist,x)

print("All function demo")
mylist = [True, True, True]
x = all(mylist)
print(mylist,x)


print("Dictionary converted to pandas dataframe")
d= { 'col1':[1,2], 'col2': [3, 4] }
df1 = pd.DataFrame(data=d)
print(df1)

print("Numpy array converted to pandas dataframe")
df3= pd.DataFrame( np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
print(df3)

df= pd.DataFrame( np.array([[2.39, -0.64, -0.91, -0.24],
                            [44.24, 42.72, 42.104, 42.622],
                            [114.003, 109.47, 109.89, 109.69],
                            [206.182, 200.5256, 200.5666, 200.132],
                            [321.60, 315.85, 315.96, 315.99]]),
                            columns=['back_left', 'back_right', 'front_left', 'front_right'])

print("Numpy array showing measured wheel rotation speeds")
print(df)
print(df.index.values)

print("We are trying to estimate which a*x^2 + b*x +c polynom would fit this data")
p=np.polyfit(df.index.values, df,2)
print(p)


# numpy.polyval(p, x)
# Evaluate a polynomial at specific values.
# np.polyval([3,0,1], 5)  # 3 * 5**2 + 0 * 5**1 + 1
# 76
#np.polyval(np.poly1d([3,0,1]), np.poly1d(5))
#poly1d([76.])
# Simulating polynom: 12t^2 + 7t - 20
print("np.polyval calculated/expected speeds at time t (this is test only")
theoretical_vaule1 = np.polyval([12,7,20], df.index.values)
print(theoretical_vaule1)


print("np.polynomial.Polynomial calculated/expected speeds at time t using 12t^2+7t-20 formula")
polynomial = np.polynomial.Polynomial([-0.51, 31, 12])
theoretical_value = polynomial(df.index.values)
print(theoretical_value)

#The all() function returns True if all items in an iterable are true, otherwise it returns False.
print("Calculating which wheels is not rotating with the right speed")
print("Test1: colums with higher error than 1")
for column in df.columns:
    if not all(df[column] - theoretical_value < 1):
        print(column)

#The any() function returns True if any item in an iterable are true, otherwise it returns False.
print("Test2")
for column in df.columns:
    if not any(df[column] - theoretical_value < 1):
        print(column)

print("Test3")
for column in df.columns:
    if any(df[column] - theoretical_value < 1):
        print(column)

print("Test4")
for column in df.columns:
    if all(df[column] - theoretical_value < 1):
        print(column)