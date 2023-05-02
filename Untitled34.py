#!/usr/bin/env python
# coding: utf-8

# Write a Python program to convert kilometers to miles?

# In[1]:


distance_km = float(input("Enter the distance in kilometers: "))
distance_miles = distance_km / 1.600
print(distance_km, "kilometers is equal to", distance_miles, "miles.")


# Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


temp_celsius = float(input("Enter the temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(temp_celsius, "degrees Celsius is equal to", temp_fahrenheit, "degrees Fahrenheit.")


# 3.Write a Python program to display calendar?

# In[3]:


import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(calendar.month(year, month))


# 4.Write a Python program to solve quadratic equation?

# In[6]:


import math
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root is", root)
else:
    print("The equation has no real roots.")


# 5.Write a Python program to swap two variables without temp variable?

# In[7]:


a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)


# In[ ]:




