log=open('NASA_access_log_Jul95')
from collections import Counter
import matplotlib.pyplot as plt




ip_address=[]

try:
    for i in log:
        print(i.split(' ')[0])

except UnicodeDecodeError:
    print()


ip_address_counter= Counter(ip_address)

plt.show()