import time

#  1 Assign an integer to a variable
great_number = 14

# 2 Assign a string to a variable
great_string = "Kirby"

# 3 Assign a float to a variable
great_float = 3.14159

# 4 Use the print function and .format() notation to print out the variable you assigned
print('O, great {} of ye {}!'.format('Captain Kirby','Malta'))

# Use each of these operators +, - , * , / , +=, = , %

x_int = 12
y_int = 10
z_int = 22

print(x_int + y_int)

print(x_int - y_int)

print(x_int * y_int)

print(x_int/y_int)

z_int += x_int
print(z_int)

print(x_int % y_int)

# 6 Use of logical operators: and, or, not

gimme_list= ['cat','dog','cow','rabbit','pikachu']
print("Here is the guest list for the tea party:{}".format(gimme_list))
time.sleep(1)

if 'cat' and 'dog' in gimme_list:
    print('Yes! Cat and dog is in the list!')
    time.sleep(1)

if 'crocodile' or 'pikachu' in gimme_list:
    print('Yes, maybe one of them is on the list')
    time.sleep(1)

if 'crocodile' not in gimme_list:
    print('Oh boy! Crocodile is not in the list... gotta add him before he gets mad, and we get eaten!')
    time.sleep(2)

# 7 use of conditional statements if, elif, else
ur_num = int(input("Give me a number between 1-20: "))
ur_range = list(range(1,20))
if ur_num > 10 and ur_num in ur_range:
    print("Number is greater than 10!")
    print(" ")
elif ur_num < 10 and ur_num in ur_range:
    print("Number is less than 10!")
    print (" ")
else:
    print("Do you know how to count?")
    print (" ")

# 8 Use of a while loop
my_num = 0
while my_num != 5:
    my_num += 1
    print (my_num)

# 9 Use of a for loop
gimme_word = input("Give me one word: ")
length_word = len(gimme_word)
counter = 0
for i in range(0,length_word):
    counter += 1
    print(counter)

print("Total letters in your word is: {}".format(counter))

# 10 Create a list and iterate through that list using a for loop to print each item out on a new line

name_list = ["Orion","Ursa Major","Cassiopeia","Lyra","Cygnus"]

for j in range(0,len(name_list)):
    print(name_list[j])
    time.sleep(0.5)

# 11 Create a tuple and iterate through it using a for loop to print each item out on a new line

fox_tuple = ('the','quick','brown','fox')
print("-- Tuple starts here --")
for k in range(0,len(fox_tuple)):
    print(fox_tuple[k])
    time.sleep(0.5)

# 12 Define a function that returns a string variable combine with
# 13 Call the function you defined above and print the result to the shell
def print_string():
    print("Printing string now...")
    print("Streeeeeennnng!")
print_string()