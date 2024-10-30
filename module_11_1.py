import requests
import pandas
import matplotlib.pyplot as plt
import numpy as np

#requests
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")

#pandas
data = pandas.read_csv('1.csv')
print(data.head())
print(data.describe())
print(data.isnull().sum())

#matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
