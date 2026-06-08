# Exercise-1

# Predict what double("22") will do. 
# Then run the code and check. Did it do what you expected? 
# Why did it return the value it did?

def double(value):
    return value * 2

#Answer
#I guess it'll return 2222. That's because any value in quotes is a string, 
# and when strings are multiplied, they repeat the characters.

def double(value):
    return value * 2

print("double is:", double("22"))   #double is: 2222

# Yes, It returned 2222 as I predicted.
# Python's operator "*" when used with a string and a number, repeats this string as "number" times,
# and it didn't convert the string "22" into number 22.


#Exercise-2

def double(number):
    return number * 3

print(double(10))


#Read the above code and write down what the bug is. How would you fix it?

# Answer
# There are two way to fix it:
# 1. Change *3 to *2.

def double(number):
    return number * 2

print(double(10))

# or

# 2. Rename the function to "triple" if we want multiply by 3 - it keeps the logic correct.

def triple(number):
    return number * 3

print(triple(10))
