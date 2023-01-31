# 1.1 Evaluate expressions to identify the data types Python assigns to variables

x = True

print(type(x)) # bool



# 1.2 Perform and analyze data and data type operations

x = 2

y = "4"

print (x + int(y))



# 1.3 Determine the sequence of execution based on operator precedence

print(3 + 4 * 2)



# 2.1 Construct and analyze code segments that use branching statements

name= "Bob"

if name=='Bob':
    print('Wassup')

else:
    print('Who are you?')


ageLimit= 18
heightLimit= 2

age= int(input('Enter your age'))
height= int(input('Enter your height'))

if age>= ageLimit:
    if height>=heightLimit:
        print('You can get your liscence')
    else:
        print('You are too young for a liscense')
else:
     print('You are too short, cant even reach the pedal')



# 2.2 Construct and analyze code segments that perform iteration

a= 20
b=10

while b<=a:
    a-=1
    if a ==15:
        print('a was equal to 15 once')
        continue
    print(a)


sum=0

for i in range(20):
    sum=sum +i
    print(sum)


# 3.1 Construct and analyze code segments that perform file input and output operations

my_file=open('kevaughn.txt', 'a')

my_file.write(' im writing from pyhton\n')

my_file.close()

my_file=open('kevaughn.txt')

for line in my_file.readlines():
    print(line, end='')



my_list=[
    "dog",
    "cat",
    "lion",
    "rat",
    "bunny"
]

print(my_list)

my_list.append('giraffe')

print(my_list[-1])

# 3.2 Construct and analyze code segments that perform console input and output operations 