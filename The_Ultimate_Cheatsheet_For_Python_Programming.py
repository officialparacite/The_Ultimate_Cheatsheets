#####Variables#####
name = "Alice"                      # string variable
pi = 3.14                           # float
count = 42                          # integer
is_valid = True                     # boolean


#####Printing#####
print(name)                         # print variable
print(f"Hello {name}")              # f-string formatting
print("Sum:", 3 + 5)                # multiple args


#####Arithmetic#####
print(3 + 5)                        # addition
print(3 - 1)                        # subtraction
print(3 * 5)                        # multiplication
print(5 / 2)                        # float division (2.5)
print(5 // 2)                       # integer division (2)
print(5 % 2)                        # modulus
print(2 ** 3)                       # exponent (8)


#####Strings#####
string = "hello world"

# Access & Slicing
string[0]                           # 'h'          → indexing
string[-1]                          # 'd'          → last char
string[0:5]                         # 'hello'      → slicing: start:end:step
len(string)                         # 11           → length

# Modify / Transform
string.replace("world", "Python")   # substitution
string.upper()                      # "HELLO WORLD"
string.lower()                      # "hello world"
string.strip()                      # remove leading/trailing whitespace
string.strip(".,!")                 # remove given chars from ends

# Searching & Checking
string.find("world")                # 6   → index of first occurrence (-1 if not found)
string.startswith("hell")           # True
string.endswith("orld")             # True
string.count("l")                   # 3
string.isdigit()                    # False
string.isalpha()                    # False

# Splitting & Joining
words = string.split()              # ['hello', 'world']  → split on whitespace
text = " ".join(words)              # "hello world"       → join list into string

# Concatenation & Formatting
print("hello" + " " + "tam")        # "hello tam"         → string concatenation
name = "Tam"
new_string = f"Hello {name}"        # f-strings (formatted string literals)


#####Lists_(arrays)#####
arr = ["one", "two", "three"]
empty_list = []                     # empty list

# Access & Slicing
arr[0]                              # "one"
arr[1:3]                            # slicing: start:end:step
len(arr)                            # length

# Add / Insert
arr.append("four")                  # add at end
arr.insert(1, "new")                # insert at index

# Remove
arr.remove("two")                   # remove by value
arr.pop(1)                          # remove by index (default: last)

# Sorting
arr.sort()                          # sort in place
sorted(arr)                         # return sorted copy

# Other operations
new_arr = arr + ["four", "five"]    # concatenate lists
min([1,2,3])                        # minimum
max([1,2,3])                        # maximum
sum([1,2,3])                        # sum of values


#####Dictionaries#####
my_dict = {"one": 1, "two": 2, "three": 3}
empty_dict = {}                     # empty dict

# Access
my_dict["one"]                      # returns 1 (KeyError if not exists)
my_dict.get("four", 4)              # safe access with default

# Add / Update
my_dict["four"] = 4                 # add or update

# Remove
my_dict.pop("three")                # remove key and return value
del my_dict["two"]                  # remove key

# Views
print(my_dict.keys())               # dict_keys(['one','two','three'])
print(my_dict.values())             # dict_values([1,2,3])
print(my_dict.items())              # dict_items([('one',1),('two',2),('three',3)])
print(list(my_dict.items()))        # list of key-value tuples

# Membership
check_one = "one" in my_dict        # True
check_five = "five" not in my_dict  # True


#####Tuples_(immutable ordered collections)#####
my_tuple = (1, 2, 3)
empty_tuple = ()

# Access
my_tuple[0]                         # 1
my_tuple[-1]                        # 3
my_tuple[0:2]                       # (1, 2)

# Immutability
# t[0] = 5                          # ❌ Error, tuples cannot be modified

# Useful functions
len(my_tuple)                       # 3
min(my_tuple)                       # 1
max(my_tuple)                       # 3
sum(my_tuple)                       # 6

# Single-element tuple (note the comma!)
single = (5,)

# Creation
my_set = {1, 2, 3}
empty_set = set()                   # {} creates an empty dict, not a set

# Add / Remove
my_set.add(4)
my_set.remove(2)                    # raises KeyError if element not found
my_set.discard(5)                   # safe remove, no error if not present
my_set.pop()                        # removes and returns an arbitrary element


#####Set_operations#####
a = {1, 2, 3}
b = {3, 4, 5}

set_union = a | b                   # union -> {1, 2, 3, 4, 5}
set_intersection = a & b            # intersection -> {3}
set_diff = a - b                    # difference -> {1, 2}
set_sym_diff = a ^ b                # symmetric difference -> {1, 2, 4, 5}

# Membership
check_three = 3 in a                # True
check_five = 5 not in a             # True


#####Conditionals#####

# If/Elif/Else
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Multiple conditions using logical operators: and, or, not
if x > 0 and x < 20:
    print("x is between 1 and 19")

if x < 0 or x > 100:
    print("x is out of range")

if not x == 10:
    print("x is not 10")

# Membership testing
my_list = [1, 2, 3]

if 2 in my_list:
    print("Found 2")

if 5 not in my_list:
    print("5 is missing")

string = ""

if not string:                      #empty check
    print("empty string")


#####For_Loops#####

arr = ["one", "two", "three"]
for item in arr:
    print(item)

# Iterate with index
for i, item in enumerate(arr):
    print(i, item)                  # 0 one, 1 two, 2 three

# Iterate over dictionary keys and values
my_dict = {"one": 1, "two": 2}
for key in my_dict:
    print(key, my_dict[key])        # iterate keys
for key, value in my_dict.items():
    print(key, value)               # iterate key-value pairs

# Iterate over a range of numbers
for i in range(5):                  # 0 to 4
    print(i)
for i in range(2, 10, 2):           # 2,4,6,8  (start, stop, step)
    print(i)


#####While_Loops#####

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue                    # skip iteration
    if i == 4:
        break                       # exit loop
    print(i)


#####Functions#####
def greeting(name):
    print(f"Hello {name}")

greeting("Tam")                     # Hello Tam

# Return values
def add(a, b):
    return a + b

result = add(2, 3)                  # 5

# Default arguments
def greet(name="World"):
    print(f"Hello {name}")

greet()                             # Hello World
greet("Tam")                        # Hello Tam

# Keyword arguments
def describe(name, age):
    print(f"{name} is {age} years old")

describe(age=25, name="Tam")        # order doesn't matter

# Variable length arguments

def sum_all(*args):                 # collects positional args as a tuple
    return sum(args)

sum_all(1, 2, 3, 4)                 # 10

def print_info(**kwargs):           # collects keyword args as a dict
    print(kwargs)

print_info(name="Tam", age=25)      # {'name': 'Tam', 'age': 25}

# Lambda/Anonymous Funtions
square = lambda x: x**2
print(square(5))                    # 25

# Often used with map, filter
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9]

# Docstrings (function documentation)
def sum_of(a, b):
    """Returns the sum of a and b"""
    return a + b

help(sum_of)                        # shows the docstring


#####File_I/O#####

# Opening and closing files
file = open("example.txt", "r")     # modes: "r", "w", "a", "rb", "wb"
content = file.read()               # read entire file
file.close()                        # always close file

# Preferred: context manager (auto-close)
with open("example.txt", "r") as file:
    content = file.read()

# Reading from files
file = open("example.txt", "r")

file.read()                         # read entire file
file.readline()                     # read one line
file.readlines()                    # read all lines into a list

file.close()

# Writing to files
with open("example.txt", "w") as file:
    file.write("Hello World\n")     # overwrite file

with open("example.txt", "a") as file:
    file.write("Another line\n")    # append to file

# Binary mode
with open("example.bin", "wb") as file:
    file.write(b"\x00\x01\x02")     # write bytes

with open("example.bin", "rb") as file:
    data = file.read()              # read bytes

# Iteration over file lines
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())         # strip removes newline

#####Command_Line_Arguments_(sys.argv is a list)#####
import sys
print(sys.argv[0])                  # script name
print(sys.argv[1:])                 # all args
len(sys.argv)                       # number of args

####Exception_handling#####

# Error Handling
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Sum:", x + y)
except ValueError:
    print("Error: Invalid number entered")  # handles non-numeric input
except Exception as e:
    print("Unexpected error:", e)           # handles any other error

#####Exit_Codes#####
import sys
sys.exit(0)                     # success (1 for failure)
