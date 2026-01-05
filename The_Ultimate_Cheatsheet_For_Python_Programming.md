
---

# Python Programming

---

## Index

| * | Table of Contents |
|---|-------------------|
| - | [Variables](#variables) |
| - | [Printing](#printing) |
| - | [Arithmetic](#arithmetic) |
| - | [Strings](#strings) |
| - | [Lists](#lists) |
| - | [Dictionaries](#dictionaries) |
| - | [Tuples](#tuples) |
| - | [Sets](#sets) |
| - | [Unpacking](#unpacking) |
| - | [Conditionals](#conditionals) |
| - | [For Loops](#for-loops) |
| - | [While Loops](#while-loops) |
| - | [Functions](#functions) |
| - | [File I/O](#file-io) |
| - | [Command Line Arguments](#command-line-arguments) |
| - | [Exception Handling](#exception-handling) |
| - | [Exit Codes](#exit-codes) |

---

## Variables

```python
name = "Alice"                      # string
pi = 3.14                           # float
count = 42                          # integer
is_valid = True                     # boolean
nothing = None                      # null/none value

# Type checking
type(name)                          # <class 'str'>
isinstance(count, int)              # True

# Type conversion
int("42")                           # string to int
float("3.14")                       # string to float
str(42)                             # int to string
bool(1)                             # int to bool (True)
list("abc")                         # ['a', 'b', 'c']
```

---

## Printing

```python
print(name)                         # print variable
print(f"Hello {name}")              # f-string formatting
print("Sum:", 3 + 5)                # multiple arguments
print("Hello", end=" ")             # custom line ending (default: \n)
print("a", "b", "c", sep=", ")      # custom separator → a, b, c

# Formatting
print(f"{pi:.2f}")                  # 3.14 (2 decimal places)
print(f"{count:05d}")               # 00042 (zero-padded)
print(f"{name:>10}")                # right-align, width 10
print(f"{name:<10}")                # left-align, width 10
print(f"{name:^10}")                # center, width 10
```

---

## Arithmetic

```python
3 + 5                               # 8 (addition)
3 - 1                               # 2 (subtraction)
3 * 5                               # 15 (multiplication)
5 / 2                               # 2.5 (float division)
5 // 2                              # 2 (integer division)
5 % 2                               # 1 (modulus)
2 ** 3                              # 8 (exponent)

# Assignment operators
x = 10
x += 5                              # x = x + 5
x -= 3                              # x = x - 3
x *= 2                              # x = x * 2
x /= 4                              # x = x / 4
x //= 2                             # x = x // 2
x **= 2                             # x = x ** 2

# Built-in math functions
abs(-5)                             # 5
round(3.7)                          # 4
round(3.14159, 2)                   # 3.14
pow(2, 3)                           # 8
divmod(17, 5)                       # (3, 2) → (quotient, remainder)

# Math module
import math
math.sqrt(16)                       # 4.0
math.floor(3.7)                     # 3
math.ceil(3.2)                      # 4
math.pi                             # 3.141592...
```

---

## Strings

```python
string = "hello world"
```

### Access & Slicing

```python
string[0]                           # 'h' (indexing)
string[-1]                          # 'd' (last char)
string[0:5]                         # 'hello' (slicing)
string[6:]                          # 'world' (from index to end)
string[:5]                          # 'hello' (start to index)
string[::2]                         # 'hlowrd' (every 2nd char)
string[::-1]                        # 'dlrow olleh' (reverse)
len(string)                         # 11 (length)
```

### Modify / Transform

```python
string.replace("world", "Python")   # 'hello Python'
string.upper()                      # 'HELLO WORLD'
string.lower()                      # 'hello world'
string.title()                      # 'Hello World'
string.capitalize()                 # 'Hello world'
string.swapcase()                   # 'HELLO WORLD'
string.strip()                      # remove leading/trailing whitespace
string.lstrip()                     # remove leading whitespace
string.rstrip()                     # remove trailing whitespace
string.strip(".,!")                 # remove specific chars from ends
```

### Searching & Checking

```python
string.find("world")                # 6 (index, -1 if not found)
string.index("world")               # 6 (raises ValueError if not found)
string.rfind("o")                   # 7 (last occurrence)
string.startswith("hell")           # True
string.endswith("orld")             # True
string.count("l")                   # 3
"world" in string                   # True

# Character checks
string.isdigit()                    # False
string.isalpha()                    # False (has space)
string.isalnum()                    # False
string.isspace()                    # False
string.islower()                    # True
string.isupper()                    # False
```

### Splitting & Joining

```python
words = string.split()              # ['hello', 'world'] (split on whitespace)
words = string.split(",")           # split on comma
parts = "a:b:c".split(":", 1)       # ['a', 'b:c'] (max 1 split)

text = " ".join(words)              # 'hello world'
text = ", ".join(["a", "b", "c"])   # 'a, b, c'

lines = "a\nb\nc".splitlines()      # ['a', 'b', 'c']
```

### Concatenation & Formatting

```python
"hello" + " " + "world"             # 'hello world'
"ha" * 3                            # 'hahaha'

name = "Tam"
f"Hello {name}"                     # f-string (Python 3.6+)
"Hello {}".format(name)             # format method
"Hello %s" % name                   # % formatting (old style)
```

---

## Lists

```python
arr = ["one", "two", "three"]
empty_list = []
nums = list(range(5))               # [0, 1, 2, 3, 4]
```

### Access & Slicing

```python
arr[0]                              # 'one'
arr[-1]                             # 'three' (last element)
arr[1:3]                            # ['two', 'three']
arr[::2]                            # every 2nd element
arr[::-1]                           # reversed list
len(arr)                            # 3
```

### Add / Insert

```python
arr.append("four")                  # add at end
arr.insert(1, "new")                # insert at index
arr.extend(["five", "six"])         # add multiple elements
arr += ["seven"]                    # concatenate
```

### Remove

```python
arr.remove("two")                   # remove by value (first occurrence)
arr.pop()                           # remove and return last
arr.pop(1)                          # remove and return at index
del arr[0]                          # delete by index
arr.clear()                         # remove all elements
```

### Sorting & Reversing

```python
arr.sort()                          # sort in place
arr.sort(reverse=True)              # sort descending
arr.reverse()                       # reverse in place
sorted(arr)                         # return sorted copy
reversed(arr)                       # return reversed iterator
```

### Searching

```python
arr.index("two")                    # index of first occurrence
arr.count("one")                    # count occurrences
"one" in arr                        # True (membership check)
```

### Other Operations

```python
new_arr = arr + ["four", "five"]    # concatenate
arr_copy = arr.copy()               # shallow copy
arr_copy = arr[:]                   # shallow copy (slicing)

min([1, 2, 3])                      # 1
max([1, 2, 3])                      # 3
sum([1, 2, 3])                      # 6
```

### List Comprehension

```python
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
matrix = [[i*j for j in range(3)] for i in range(3)]
```

---

## Dictionaries

```python
my_dict = {"one": 1, "two": 2, "three": 3}
empty_dict = {}
from_pairs = dict([("a", 1), ("b", 2)])
```

### Access

```python
my_dict["one"]                      # 1 (KeyError if not exists)
my_dict.get("one")                  # 1 (None if not exists)
my_dict.get("four", 4)              # 4 (default if not exists)
```

### Add / Update

```python
my_dict["four"] = 4                 # add or update
my_dict.update({"five": 5})         # update with another dict
my_dict.setdefault("six", 6)        # set only if key doesn't exist
```

### Remove

```python
my_dict.pop("three")                # remove and return value
my_dict.pop("missing", None)        # with default (no error)
del my_dict["two"]                  # delete key
my_dict.clear()                     # remove all
```

### Views & Iteration

```python
my_dict.keys()                      # dict_keys(['one', 'two', 'three'])
my_dict.values()                    # dict_values([1, 2, 3])
my_dict.items()                     # dict_items([('one', 1), ...])

for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
```

### Membership

```python
"one" in my_dict                    # True (checks keys)
"five" not in my_dict               # True
```

### Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}           # {0: 0, 1: 1, 2: 4, ...}
filtered = {k: v for k, v in my_dict.items() if v > 1}
```

---

## Tuples

```python
my_tuple = (1, 2, 3)
empty_tuple = ()
single = (5,)                       # single element (note the comma!)
from_list = tuple([1, 2, 3])
```

### Access

```python
my_tuple[0]                         # 1
my_tuple[-1]                        # 3
my_tuple[0:2]                       # (1, 2)
```

### Immutability

```python
# my_tuple[0] = 5                   # ❌ TypeError: tuples cannot be modified
```

### Operations

```python
len(my_tuple)                       # 3
min(my_tuple)                       # 1
max(my_tuple)                       # 3
sum(my_tuple)                       # 6
my_tuple.count(1)                   # 1
my_tuple.index(2)                   # 1

# Concatenation
(1, 2) + (3, 4)                     # (1, 2, 3, 4)
(1, 2) * 2                          # (1, 2, 1, 2)
```

---

## Sets

```python
my_set = {1, 2, 3}
empty_set = set()                   # {} creates empty dict, not set!
from_list = set([1, 2, 2, 3])       # {1, 2, 3} (duplicates removed)
```

### Add / Remove

```python
my_set.add(4)                       # add element
my_set.update([5, 6])               # add multiple elements
my_set.remove(2)                    # remove (KeyError if not found)
my_set.discard(5)                   # remove (no error if not found)
my_set.pop()                        # remove and return arbitrary element
my_set.clear()                      # remove all
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b                               # union: {1, 2, 3, 4, 5}
a & b                               # intersection: {3}
a - b                               # difference: {1, 2}
a ^ b                               # symmetric difference: {1, 2, 4, 5}

a.union(b)                          # same as |
a.intersection(b)                   # same as &
a.difference(b)                     # same as -
a.symmetric_difference(b)           # same as ^

a.issubset(b)                       # is a subset of b?
a.issuperset(b)                     # is a superset of b?
a.isdisjoint(b)                     # no common elements?
```

### Membership

```python
3 in a                              # True
5 not in a                          # True
```

### Set Comprehension

```python
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

---

## Unpacking

### Basic Unpacking

```python
a, b = [1, 2]                       # a=1, b=2
x, y, z = (10, 20, 30)              # works with tuples
```

### Extended Unpacking

```python
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
*head, tail = [10, 20, 30]              # head=[10, 20], tail=30
head, *tail = [10, 20, 30]              # head=10, tail=[20, 30]
```

### Ignore Values

```python
a, _, b = [1, 99, 2]                # a=1, b=2 (ignore middle)
a, *_, b = [1, 2, 3, 4, 5]          # a=1, b=5 (ignore middle)
```

### Nested Unpacking

```python
(x1, x2), (y1, y2) = [(1, 2), (3, 4)]   # x1=1, x2=2, y1=3, y2=4
```

### Function Arguments

```python
def add(x, y, z):
    return x + y + z

nums = [1, 2, 3]
add(*nums)                          # 6 (unpack list as args)

d = {"x": 1, "y": 2, "z": 3}
add(**d)                            # 6 (unpack dict as kwargs)
```

### Merge Collections

```python
# Merge lists
merged = [*list1, *list2]

# Merge dicts
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}               # {'a': 1, 'b': 2}
merged = d1 | d2                    # Python 3.9+ (same result)
```

---

## Conditionals

### If / Elif / Else

```python
x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### Logical Operators

```python
if x > 0 and x < 20:
    print("Between 1 and 19")

if x < 0 or x > 100:
    print("Out of range")

if not x == 10:
    print("Not 10")
```

### Membership Testing

```python
my_list = [1, 2, 3]

if 2 in my_list:
    print("Found")

if 5 not in my_list:
    print("Missing")
```

### Truthiness / Empty Checks

```python
# Falsy values: None, False, 0, 0.0, '', [], {}, set()

if not string:                      # empty string check
    print("Empty")

if my_list:                         # non-empty list check
    print("Has items")

if value is None:                   # None check
    print("Is None")

if value is not None:
    print("Has value")
```

### Ternary Operator

```python
result = "Yes" if condition else "No"
value = x if x > 0 else 0
```

### Comparison Chaining

```python
if 0 < x < 10:                      # equivalent to: x > 0 and x < 10
    print("Single digit")
```

---

## For Loops

### Basic Iteration

```python
arr = ["one", "two", "three"]

for item in arr:
    print(item)
```

### With Index

```python
for i, item in enumerate(arr):
    print(i, item)                  # 0 one, 1 two, 2 three

for i, item in enumerate(arr, start=1):
    print(i, item)                  # 1 one, 2 two, 3 three
```

### Dictionary Iteration

```python
my_dict = {"one": 1, "two": 2}

for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

for value in my_dict.values():
    print(value)
```

### Range

```python
for i in range(5):                  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10):              # 2, 3, ..., 9
    print(i)

for i in range(0, 10, 2):           # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):          # 10, 9, ..., 1
    print(i)
```

### Multiple Iterables

```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(name, age)                # Alice 25, Bob 30
```

### Loop with Else

```python
for item in arr:
    if item == "target":
        break
else:
    print("Not found")              # runs if no break occurred
```

---

## While Loops

### Basic While

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Break and Continue

```python
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue                    # skip to next iteration
    if i == 7:
        break                       # exit loop
    print(i)
```

### While with Else

```python
while condition:
    if found:
        break
else:
    print("Loop completed")         # runs if no break occurred
```

### Infinite Loop

```python
while True:
    user_input = input("Enter (q to quit): ")
    if user_input == 'q':
        break
```

---

## Functions

### Basic Function

```python
def greet(name):
    print(f"Hello {name}")

greet("Tam")                        # Hello Tam
```

### Return Values

```python
def add(a, b):
    return a + b

result = add(2, 3)                  # 5

# Multiple return values
def get_stats(nums):
    return min(nums), max(nums), sum(nums)

low, high, total = get_stats([1, 2, 3])
```

### Default Arguments

```python
def greet(name="World"):
    print(f"Hello {name}")

greet()                             # Hello World
greet("Tam")                        # Hello Tam
```

### Keyword Arguments

```python
def describe(name, age):
    print(f"{name} is {age}")

describe(age=25, name="Tam")        # order doesn't matter
```

### Variable Length Arguments

```python
# *args: positional arguments as tuple
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)                 # 10

# **kwargs: keyword arguments as dict
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Tam", age=25)

# Combined
def func(a, b, *args, **kwargs):
    pass
```

### Lambda Functions

```python
square = lambda x: x ** 2
square(5)                           # 25

add = lambda x, y: x + y
add(2, 3)                           # 5

# With map, filter, sorted
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))       # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x%2==0, nums))    # [2, 4]
sorted_list = sorted(nums, key=lambda x: -x)    # [5, 4, 3, 2, 1]
```

### Docstrings

```python
def sum_of(a, b):
    """
    Returns the sum of a and b.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

help(sum_of)                        # shows docstring
sum_of.__doc__                      # access docstring
```

### Type Hints (Python 3.5+)

```python
def greet(name: str) -> str:
    return f"Hello {name}"

def add(a: int, b: int) -> int:
    return a + b

from typing import List, Dict, Optional

def process(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def find(items: List[str], target: str) -> Optional[int]:
    return items.index(target) if target in items else None
```

---

## File I/O

### Opening Files

```python
# Basic open/close
file = open("example.txt", "r")
content = file.read()
file.close()

# Context manager (preferred - auto-closes)
with open("example.txt", "r") as file:
    content = file.read()
```

### File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (overwrites) |
| `a` | Append |
| `x` | Create (error if exists) |
| `r+` | Read and write |
| `rb` | Read binary |
| `wb` | Write binary |

### Reading

```python
with open("example.txt", "r") as f:
    content = f.read()              # entire file as string
    
with open("example.txt", "r") as f:
    line = f.readline()             # single line
    
with open("example.txt", "r") as f:
    lines = f.readlines()           # all lines as list

# Iterate line by line (memory efficient)
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Writing

```python
# Overwrite
with open("example.txt", "w") as f:
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Append
with open("example.txt", "a") as f:
    f.write("New line\n")
```

### Binary Mode

```python
# Write bytes
with open("example.bin", "wb") as f:
    f.write(b"\x00\x01\x02")

# Read bytes
with open("example.bin", "rb") as f:
    data = f.read()
```

### File Operations (os module)

```python
import os

os.path.exists("file.txt")          # check if exists
os.path.isfile("file.txt")          # is a file?
os.path.isdir("folder")             # is a directory?
os.path.getsize("file.txt")         # file size in bytes
os.remove("file.txt")               # delete file
os.rename("old.txt", "new.txt")     # rename
os.listdir(".")                     # list directory contents
os.makedirs("path/to/dir")          # create directories
```

---

## Command Line Arguments

```python
import sys

sys.argv[0]                         # script name
sys.argv[1]                         # first argument
sys.argv[1:]                        # all arguments (excluding script name)
len(sys.argv)                       # number of arguments (including script name)
```

### Using argparse (recommended)

```python
import argparse

parser = argparse.ArgumentParser(description="My script")
parser.add_argument("filename", help="Input file")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
parser.add_argument("-n", "--number", type=int, default=10, help="Number of items")

args = parser.parse_args()

print(args.filename)
print(args.verbose)
print(args.number)
```

---

## Exception Handling

### Try / Except

```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
```

### Try / Except / Else / Finally

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("Success!")              # runs if no exception
finally:
    print("Cleanup")               # always runs
```

### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Re-raise exception
try:
    risky_operation()
except Exception:
    print("Error occurred")
    raise                          # re-raise the exception
```

### Common Exceptions

| Exception | Description |
|-----------|-------------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong type |
| `KeyError` | Dict key not found |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File not found |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Attribute not found |
| `ImportError` | Import failed |

---

## Exit Codes

```python
import sys

sys.exit(0)                         # success
sys.exit(1)                         # failure
sys.exit("Error message")           # exit with message (code 1)
```

---

[↑ Back to Index](#index)
