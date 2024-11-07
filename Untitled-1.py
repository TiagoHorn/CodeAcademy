#%%
# Phyton leasons
# or, and
# and expression is true if one of the values is true, in this case both are true
import random
(4 <= 2 * 3) and (7 + 1 == 8)

4 * 5 <= 21 - 1
3 ** 2 + 1 != 30/3

x = 0

if x == 0:
    print("x os equal to zero")
elif x >= 0:
    print("x is greater than zero")
else:
    print("x is less than zero")

x = 5

if x <= 2:
    print("This is printed")
if x <= 4:
    print("This is also printed")
if x <= 6:
    print("Is this printed?")
if x <= 8:
    print("This might be printed")
  # %%
name = "Tiago"
question = "" or ""
answer = ""

random_number = random.randint(1, 11)
print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "That is impossible"
elif random_number == 11:
    answer = "I can`t answer that question"
else:
    answer = "Error"

if name == "":
    print(" Question: " + question)
else:
    print(name + " ask: " + question)

if question == "":
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
    print(name + " ask: " + question)
    print("Magic 8-Ball`s answer:" + answer)
# %%
minha_lista = ("car", "moto", "dia")
len(minha_lista)
mylist = ["a", "b", "c", "d", "e"]
print(mylist[2:5])
# mylist.pop()
# print(mylist)
mylist[1:3]
# print(mylist
list(range(2, 14, 4))


toppings = ["pepperoni", "pineaple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 1]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell" + str(num_pizzas) + "diferent kinds pizza!")
# %%
pizza_and_price = [[2, "pineaple"], [6, "pepperoni"], [1, "cheese"], [
    3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_price)
# %%
pizza_and_price.sort()
# %%
cheapest_pizza = pizza_and_price[0]
# %%
priciest_pizza = pizza_and_price[-1]
pizza_and_price.pop()
# %%
pizza_and_price.append([2.5, "peppers"])

three_cheapest = pizza_and_price[:3]
print(three_cheapest)
# %%
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Dpggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# While Loop Walkthrough
# count = 0
# print("Starting While Loop")
# while count <= 3:
#   # Loop Body
#   # Print if the condition is still true
#   print("Loop Iteration - count <= 3 is still true")
#   # Print the current value of count
#   print("Count is currently " + str(count))
#   # Increment count
#   count += 1
#   print(" ----- ")
# print("While Loop ended")

# Your code below:
countdown = 10
while countdown >= 0:

    print(countdown)
    countdown -= 1
print("We have liftoff!")

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Your code below:
length = len(python_topics)
index = 0
while index < length:
    print("I am learning about" + python_topics[index])
    index += 1

    og_breeds_available_for_adoption = [
        "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element
    print(scoops_sold)

    # %%
number = [2, -1, 79, 33, -45]
only_negative_number = []

for num in number:
    if num < 0:
        only_negative_number.append(num * 2)
print(only_negative_number)
# %%
number = [2, -1, 79, 33, -45]
double = [num * 2 if num < 0 else num * 3 for num in number]
print(double)
# %%
single_digits = range(10)
squares = []

for item in single_digits:
    print(item)
    squares.append(item**2)

print(squares)

cubes = [item**3 for item in single_digits]
print(cubes)
# %%
[i-1 for i in range(5)]

i = 1
while i <= 10:
    print(i)
    i += 1

# %%
numbers = [1, 1, 2, 3]
for number in numbers:
    if number % 2 == 0:
        break
    print(number)

numbers = [1, 1, 2, 3]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# %%
grouped_topics = [["Algorithms", "Data Structures", "AI"],
                  ["Linear Regression", "SQL"]]
for sublist in grouped_topics:
    for sublist_element in sublist:
        print(sublist_element)
# %%
hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
    total_price += price
avarage_price = (total_price / len(prices))
print("Avarage Price:${0}".format(avarage_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("total_revenue:${0}".format(total_revenue))

avarage_daily_revenue = total_revenue / 7
print("avarage_daily_revenue :${0}".format(avarage_daily_revenue))

cuts_under_30 = [hairstyles[i]
                 for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)

####
# %%
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

def f_to_c(f_tem):
    return (f_tem - 32) * 5/9


f100_in_celsius = f_to_c(100)


def c_to_f(c_temp):
    return (c_temp * 9/5) + 32


c0_in_fahrenheit = c_to_f(0)


def get_force(mass, acceleration):
    return mass * acceleration


train_mass = get_force(train_mass, train_acceleration)
print(train_mass)
print("“The GE train supplies " + str(train_mass) + " Newtons of force.")


def get_energy(mass, c=3*10**8):
    return mass * c**2


bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance


print(get_work(train_mass, train_acceleration, train_distance))

# %%Scope example


def welcome_user(name):
    greeting = "Hello " + name + "!"
    print(greeting)


welcome_user("User")

balance = 12.55
name = "Lilia"


def withdraw_money(amount):
    result = balance - amount
    print("Hello " + name + " your balance remaining is: $" + str(result))
    return amount


withdraw_money(2)
print("Save your money " + name + "!")

# scope and nested functions
# Nested functions provide a great example of how scope is determined in our program.
# Typically, the order of scope follows the pattern where inner functions are able to access outer function variables,
# but outer functions are not able to access inner function variables. Here is what that looks like in code:


def outer_func():
    location = "Inside the outer function!"

    def inner_func():
        location = "Inside the inner function!"
        print(location)

    inner_func()

    print(location)


outer_func()
# %%
num1 = 6
num2 = 3

# Write your if statement here
if num1 + num2 != 10:
    not_ten = True
else:
    not_ten = False

# %%


def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False


print(in_range(10, 10, 10))

print(in_range(5, 10, 20))

# %%


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


print(same_name("Vitor", "Tiago"))

print(same_name("Diego", "Diego"))

# %% Always false


def always_false(num):
    if num > 0 and num < 0:
        return True
    else:
        return False


print(always_false(0))
print(always_false(1))
print(always_false(-1))

# %%movie Review


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    if rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"


print(movie_review(6))
print(movie_review(3))
print(movie_review(10))

# %% Max number


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It`s a tie!"


print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))

# %% 
def append_size(my_list):
    my_list.append(len(my_list))
    return my_list


print(append_size([23, 42, 108]))
#%% Append Sum
def append_sum(my_list):
    my_list.append(my_list [-1] + my_list [-2])
    my_list.append(my_list [-1] + my_list [-2])
    my_list.append(my_list [-1] + my_list [-2])
    return my_list

print(append_sum([1, 1, 2]))

#%%
# Define the append_sum function
def append_sum(my_list):
  for i in range(3):
    # Get the sum of last two elements of the list and append it to the list
    my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))

#%% Larger List
def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    elif len(my_list1) <= len(my_list2):
        return my_list2[-1]
    else:
        return my_list1[-1]
    
print(larger_list([23, 12, 21], [1,23]))
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#%% More than N
def more_than_n(my_list, item, n):
    if my_list.count(item) > n:
        return True
    else:
        return False
    
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2,], 2, 3))

#%% combine a sort
def combine_sort(my_list1, my_list2):
    unsorted = my_list1 + my_list2
    sortedList = sorted(unsorted)
    return sortedList

print(combine_sort([4, 10, 2,5], [-10, 2, 5, 10]))

#%% loop review
def odd_nums(my_list):
    for item in my_list:
        if item % 2 == 1:
            print(item)
            
print(odd_nums([4, 7, 9, 10, 13]))

#%% divisible by ten
def divisible_by_ten(nums):
    count = 0
    for number in nums:
     if (number % 10 == 0):
         count += 1
    return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

#%% greetings (saudações)
def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)
    return new_list
    
print(add_greetings(["Owen", "Max", "Sophie"]))

#%%Delete starting Even Numbers (remove os numeros pares ate encontrar um numero impar ou acabar os numeros)
def delete_starting_even(my_list):
    while (len(my_list) > 0 and my_list[0] % 2 == 0):
        my_list = my_list[1:]
    return my_list
print(delete_starting_even([4, 8, 10, 11, 12, 15]))

#%% odd indices (ele cria uma nova lista com o item a cada 2 numeros)
def odd_indices(my_list):
    new_list = []
    for index in range(1, len(my_list), 2):
        new_list.append(my_list[index])
    return new_list
print(odd_indices([4, 3, 7, 10, 11, -2, 1, 6, 8, 13]))

#%% exponents 
def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list
print(exponents([2, 3, 4], [2, 3]))

#%% esse codigo remove todos os numeros impares
def odd_nums(lst):
    for item in lst:
        if item % 2 == 1:
            print(item)
print(odd_nums([4, 8, 3, 10, 7, 2, 11, 13, 17]))

#%% larger sum
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0 
    for number in lst1:
        sum1 += number
    for num in lst2:
        sum2 += number
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))