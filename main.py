log=open('NASA_access_log_Jul95')
from collections import Counter
import matplotlib.pyplot as plt




# ip_address=[]

# try:
#     for i in log:
#         ip_address.append(i.split(' ')[0])

# except UnicodeDecodeError:
#     print()


# ip_address_counter= Counter(ip_address)

# result = {key:value for (key, value) in ip_address_counter.items() if value > 500}
# print(result)


# ip_address_counter= Counter(result)

# print(ip_address)

# plt.bar(ip_address_counter.keys(), ip_address_counter.values())


# plt.show()

dates=[]

try:
    for i in log:
        dates.append(i.split(' ')[3])
        dates.append(i.split(':')[0])

except UnicodeDecodeError:
    print()


dates_counter= Counter(dates)

result = {key:value for (key, value) in dates_counter.items() if value > 500}
print(result)


dates_counter= Counter(result)

print(dates)

plt.bar(dates_counter.keys(), dates_counter.values())


plt.show()
