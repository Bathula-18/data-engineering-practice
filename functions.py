# practice of functions in python

# function to clean price value
def clean_price(price):
    if price == "":
        return 0
    return int(price)


# testing the function
value1 = clean_price("150")
value2 = clean_price("")

print("Value 1:", value1)
print("Value 2:", value2)


# function to convert text to uppercase
def convert_upper(text):
    return text.upper()

name = convert_upper("Sai")
print("Uppercase name:", name)
