
from collections import Counter
import matplotlib.pyplot as plt

# fruits=[
#     'banana',
#     'apple', 'apple',
#     'orange', 'orange', 'orange',
#     'cherry', 'cherry', 'cherry', 'cherry'

# ]

# fruit_counter= Counter(fruits)

# print(fruit_counter.keys())
# print(fruit_counter.values())

# plt.bar(fruit_counter.keys(), fruit_counter.keys())

# plt.show()


fruits={'cherry': 4, 'orange': 3, 'apple': 2, 'banana': 1}
print('Original')
print(fruits)

print('Filter: Greater than 2')
result = {key:value for (key, value) in fruits.items() if value > 2}
print(result)

fruit_counter= Counter(result)

print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys(), fruit_counter.values())

plt.show()
