# practice of loops (for and while)

# -------- FOR LOOP EXAMPLES --------

# loop through a list
items = ["pen", "book", "bottle"]

for item in items:
    print("Item:", item)


# loop using range
for i in range(5):
    print("Count:", i)


# loop with condition (even numbers)
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print("Even number:", number)



# -------- WHILE LOOP EXAMPLES --------

# basic while loop
count = 0

while count < 3:
    print("While count:", count)
    count = count + 1


# while loop with condition
num = 1

while num <= 5:
    print("Number:", num)
    num += 1
