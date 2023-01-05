log=open('NASA_access_log_Jul95')
from collections import Counter
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


# ip_address=[]

# plt.xlabel('IP Adressess')
# plt.ylabel('Frequency')
# plt.title('Barplot')

# try:
#     for i in log:
#         ip_address.append(i.split(' ')[0])

# except UnicodeDecodeError:
#     print()


# ip_address_counter= Counter(ip_address)

# result = {key:value for (key, value) in ip_address_counter.items() if value > 8000}
# print(result)
# bar_colors = ['tab:red', 'tab:blue', 'tab:green',]

# ip_address_counter= Counter(result)

# print(ip_address)

# plt.bar(ip_address_counter.keys(), ip_address_counter.values(), color=bar_colors)

# plt.show()

dates=[]
plt.xlabel('Dates')
plt.ylabel('Visitors')
plt.title('Barplot')


try:
    for i in log:
        dates.append(i.split(' ')[3].split(':')[0])

except UnicodeDecodeError:
    print(i)
    print()




dates_counter= Counter(dates)

result = {key:value for (key, value) in dates_counter.items() if value > 500 }
print(result)
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']


dates_counter= Counter(result)

# print(dates)

plt.bar(dates_counter.keys(), dates_counter.values(),color=bar_colors, width=0.4)

  

plt.xticks(rotation=45)



plt.show()






