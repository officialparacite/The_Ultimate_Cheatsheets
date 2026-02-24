---

# Object-Oriented Programming In Python

---

## Index

---


| * | Table of Contents |
|---|-------------------|
| - | [Classes](#classes) |
| - | [Objects](#objects) |
| - | [The `__init__` Method](#the-__init__-method) |
| - | [Instance Methods](#instance-methods) |
| - | [Class vs Instance Attributes](#class-Attributes-vs-instance-attributes) |
| - | [Functions vs Methods](#functions-vs-methods) |
| - | [Encapsulation](#encapsulation) |
| - | [Abstraction](#abstraction) |
| - | [Inheritance](#inheritance) |
| - | [Polymorphism](#polymorphism) |
| - | [Class & Static Methods](#class--static-methods) |
| - | [Properties](#properties) |
| - | [Class & Static Methods](#class-&-static-methods) |


---

## Classes

---

A **class** is a blueprint for creating custom types in Python. If you squint really hard, it's kinda like a dictionary in that it usually stores name-value pairs — except instead of just data, it can also store behavior (functions).

```python
# Defines a new class called "Soldier"
# with three properties: health, armor, damage
class Soldier:
    health = 5
    armor = 3
    damage = 2
```

Just like a string, integer, or float is a type, a class is also a type — but instead of being a built-in type, it's a **custom type you define yourself**.

---

## Objects

---

If a class is a **blueprint**, what’s an **object**?

An object is a **specific instance of a class created in memory**.

Think of it like this:

* A class describes what something *should look like*
* An object is the *actual thing* built from that description

## A Simple Example

In Python:

```python
x = 5
```

Here’s what’s happening conceptually:

* `int` → the **class (type)**
* `5` → an **instance of `int`**
* `x` → a **name that refers to that instance**

So in words:

* `int` is the class
* `5` is an object of type `int`
* `x` refers to that object

You can confirm this:

```python
print(type(x))  # <class 'int'>
```

In Python, **everything is an object** (numbers, strings, lists, functions and everything)

## Comparing to Other Languages

In Java or C++ you might write:

```java
int x;
```

This declares `x` as a variable of type `int`.

In Python:

```python
x = 5
```

You don’t declare the type explicitly. Instead:

* An object (`5`) is created
* `x` is assigned to refer to that object
* The object itself knows its type (`int`)

Python variables don’t store values directly — they store **references to objects**.

## Creating Your Own Objects

Now let’s define our own class:

```python
class Dog:
    pass

my_dog = Dog()
```

Here’s what’s happening:

* `Dog` → the class
* `Dog()` → creates a new instance (an object)
* `my_dog` → refers to that object

Every time you call `Dog()`, Python creates a **new, separate object in memory**.

---

## The `__init__` Method

---

`__init__` is a special method that runs **automatically** whenever a new object is created. You use it to give each object its own unique starting values. It’s used to initialize the object’s starting values.

`self` is just a reference to the object being created, it's how the object refers to itself.

> [!Note]
> Objects Have Their Own Data

## Example

```python
class Soldier:
    def __init__(self, health, armor, damage):
        self.health = health
        self.armor = armor
        self.damage = damage
```

When we create objects:

```python
aragorn = Soldier(100, 50, 25)
boromir = Soldier(80, 40, 20)
```

Behind the scenes, Python:

1. Creates a new empty object
2. Calls `__init__` on it
3. Passes the new object in as `self`

Conceptually, this is similar to:

```python
Soldier.__init__(aragorn, 100, 50, 25)
```

Now each object has its own independent data:

```python
print(aragorn.health)   # 100
print(boromir.health)   # 80
```

Changing one does not affect the other:

```python
aragorn.health = 10
print(aragorn.health)   # 10
print(boromir.health)   # 80
```

## What is `self`?

`self` refers to the specific instance being initialized.

It’s how each object stores its own data.

Without `self`, Python wouldn’t know which object the attributes belong to.

---

## Instance Methods

---

Methods are just **functions that belong to a class**. They define what an object can *do*, not just what it *is*.

Every instance method takes `self` as its first argument so the method knows which object it's acting on.

```python
class Soldier:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f"Dealt {self.damage} damage!")

    def is_alive(self):
        return self.health > 0

aragorn = Soldier(100, 25)
orc = Soldier(50, 10)

aragorn.attack(orc)                 # Dealt 25 damage!
print(orc.health)                   # 25
print(orc.is_alive())               # True
```

> [!Note]
> When you call `aragorn.attack(orc)` you only pass `orc` — Python automatically passes `aragorn` as `self` behind the scenes.

---

## Class Attributes vs Instance Attributes

---

There are two places an attribute can live:

- **Class attributes** are defined directly on the class and **shared by all objects** of that class.
- **Instance attributes** are **unique to each object**.

```python
class Archer:
    species = "Human"               # class attribute — shared by all archers

    def __init__(self, name):
        self.name = name            # instance attribute — unique per archer

legolas = Archer("Legolas")
bard = Archer("Bard")

print(legolas.species)              # Human
print(bard.species)                 # Human (same — it's shared)
print(legolas.name)                 # Legolas
print(bard.name)                    # Bard (different — it's per-object)

# Changing a class attribute affects ALL instances
Archer.species = "Elf"
print(legolas.species)              # Elf
print(bard.species)                 # Elf
```

---

## Functions vs Methods

---

* **Functions** are defined independently and are **not tied to any object**.
* **Methods** are functions defined inside a class and are **tied to an object**.

```python
# Function — standalone
def greet(name):
    return f"Hello, {name}!"

print(greet("Legolas"))
```

```python
class Archer:
    def __init__(self, name):
        self.name = name

    # Method — tied to an instance
    def greet(self):
        return f"Hello, I am {self.name}!"

legolas = Archer("Legolas")

print(legolas.greet())
```

---

## What’s the Real Difference?

---

### Function

* Lives outside a class
* Doesn’t automatically know about objects
* You must pass everything it needs

```python
def describe_archer(name):
    return f"{name} is ready."
```

### Method

* Lives inside a class
* Automatically receives the object (`self`)
* Can access instance attributes directly

```python
def describe(self):
    return f"{self.name} is ready."
```

When you call:

```python
legolas.describe()
```

Python automatically does:

```python
Archer.describe(legolas)
```

That’s why `self` works.

---

## Encapsulation

---

Encapsulation is the idea of **bundling data and behavior together** inside a class, and **controlling access** to that data from the outside world.

In Python, encapsulation is handled through **naming conventions**:

- `name` → public, anyone can access it
- `_name` → protected, purely a convention — signals "internal use only" but Python does nothing special with it
- `__name` → private, Python triggers **name mangling** and renames it to `_ClassName__name` behind the scenes, making accidental access harder

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._account_id = 12345    # protected — convention only, still accessible
        self.__balance = balance    # private — name mangled by Python

    def deposit(self, amount):
        if self.__validate(amount):     # private method called internally
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __validate(self, amount):       # private method
        return amount > 0

account = BankAccount("Aragorn", 1000)

print(account.owner)                        # Aragorn — fine
print(account._account_id)                  # 12345 — works, but frowned upon
print(account.get_balance())                # 1000 — correct way to access balance
print(account.__balance)                    # AttributeError
print(account._BankAccount__balance)        # 1000 — mangled name, accessible if you really want it
account.__validate(500)                     # AttributeError — private methods work the same way
```

## Why Does This Matter?

Without encapsulation, any part of your code could reach in and modify an object's data directly.

- Prevent accidental misuse
- Make it easier to change internals later without breaking other code
- Keep related data and logic together in one place

> [!Note]
> Python doesn't enforce encapsulation the way Java or C++ do. Neither `_name` nor `__name` are truly locked away — `_name` is just a naming convention, and `__name` adds friction through name mangling.

---

## Abstraction

---

The terms "abstraction" and "encapsulation" mostly just emphasize different aspects of the same concept:

- Abstraction focuses on exposing essential features while hiding complexity
- Encapsulation focuses on bundling data with methods and restricting direct access to implementation details

---

## Inheritance

---

Inheritance lets a class **take on the attributes and methods of another class**.

The class being inherited from is called the **parent** (or base) class. The class doing the inheriting is called the **child** (or derived) class.

```python
class Soldier:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} dealt {self.damage} damage!")

    def is_alive(self):
        return self.health > 0

class Archer(Soldier):      # Archer inherits from Soldier
    pass

legolas = Archer("Legolas", 100, 25)

legolas.attack(orc)         # works — inherited from Soldier
print(legolas.is_alive())   # True — inherited from Soldier
```

Just by passing `Soldier` into `Archer`, the child class gets everything the parent has for free.

## Extending the Child Class

A child class isn't limited to what the parent gives it — it can add its own attributes and methods on top. If you need to add new attributes, you'll need to define `__init__` in the child and call `super().__init__()` to make sure the parent's setup still runs. If you don't need any new attributes however, you can skip `__init__` entirely and Python will walk up to the parent and use its `__init__` automatically:

```python
# no new attributes — skip __init__ entirely, Soldier's runs automatically
class Archer(Soldier):
    def shoot(self, target):
        target.health -= self.damage
        print(f"{self.name} fired an arrow!")

# new attributes — define __init__ and call super() first
class Archer(Soldier):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)  # call the parent's __init__
        self.arrows = arrows                    # then add something new

    def shoot(self, target):
        if self.arrows > 0:
            target.health -= self.damage
            self.arrows -= 1
            print(f"{self.name} shot an arrow! {self.arrows} left.")
        else:
            print("Out of arrows!")

legolas = Archer("Legolas", 100, 25, 30)

legolas.attack(orc)     # inherited from Soldier
legolas.shoot(orc)      # unique to Archer
```

> [!Note]
> You **always** need to call `super().__init__()` if you're defining a child `__init__` — without it the parent's `__init__` never runs and the object won't have any of the parent's attributes.

## Overriding Methods

A child class can also **override** a parent method — replacing it with its own version:

```python
class Archer(Soldier):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)
        self.arrows = arrows

    def attack(self, target):                   # overrides Soldier's attack
        if self.arrows > 0:
            target.health -= self.damage * 2    # archers deal double damage
            self.arrows -= 1
            print(f"{self.name} fired an arrow for {self.damage * 2} damage!")
        else:
            super().attack(target)              # fall back to Soldier's attack if out of arrows
            print(f"{self.name} attacks with fists!")

legolas = Archer("Legolas", 100, 25, 3)
orc = Soldier("Orc", 200, 10)

legolas.attack(orc)     # uses Archer's version
```

When Python looks up a method, it checks the **child class first**, then works its way up to the parent. This is called the **method resolution order (MRO)**.

## Why Use Inheritance?

Without inheritance you'd end up copying the same attributes and methods across multiple classes. If you ever needed to change something shared, you'd have to update it everywhere. Inheritance lets you define shared behavior once in the parent and have all child classes benefit automatically.

> [!Note]
> Inheritance is powerful but easy to overuse.

---

## Polymorphism

---

Polymorphism means **different objects can respond to the same method call in different ways**.

The idea is simple: if multiple classes share a method name, you can call that method on any of them without caring about what type they are. Each object handles it in its own way.

> [!Note]
> Only the method name needs to match for polymorphism to apply — Python doesn't enforce matching signatures the way other languages do.

```python
class Soldier:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} strikes for {self.damage} damage!")

class Archer(Soldier):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)
        self.arrows = arrows

    def attack(self, target):               # same method name, different behavior
        target.health -= self.damage * 2
        print(f"{self.name} fires an arrow for {self.damage * 2} damage!")

class Mage(Soldier):
    def attack(self, target):               # same method name, different behavior again
        target.health -= self.damage * 3
        print(f"{self.name} casts a spell for {self.damage * 3} damage!")
```

Now here's where polymorphism shines — you can loop over a mix of different objects and call the same method on all of them:

```python
orc = Soldier("Orc", 200, 10)

party = [
    Soldier("Boromir", 100, 25),
    Archer("Legolas", 100, 20, 30),
    Mage("Gandalf", 80, 30)
]

for member in party:
    member.attack(orc)      # each one does it differently

# Boromir strikes for 25 damage!
# Legolas fires an arrow for 40 damage!
# Gandalf casts a spell for 90 damage!
```

Python doesn't care what type each object in `party` is — it just calls `attack()` and lets each object handle it in its own way.

---

## Operator Overloading

---

Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the `+` operator works for built-in types like integers and strings:

```python
print(3 + 4)
# 7

print("three " + "four")
# three four
```

Custom classes on the other hand don't have any built-in support for those operators:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

But we can add our own support! If we create an `__add__(self, other)` method on our class, the Python interpreter will use it when instances of the class are being added with the `+` operator. The name of the second parameter (`other` in this example) is just a convention — you can use any valid parameter name:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
```

When `p1 + p2` is executed, under the hood the Python interpreter just calls `p1.__add__(p2)`. You're not changing how `+` works globally — only how it behaves when your specific class is involved. Everything else behaves as normal.

The same idea extends to other operators too. Each one maps to a dunder method that you can define on your class:

| Operator | Dunder Method | Triggered When |
|----------|--------------|----------------|
| `+` Addition | `__add__` | `a + b` |
| `-` Subtraction | `__sub__` | `a - b` |
| `*` Multiplication | `__mul__` | `a * b` |
| `**` Power | `__pow__` | `a ** b` |
| `/` Division | `__truediv__` | `a / b` |
| `//` Floor Division | `__floordiv__` | `a // b` |
| `%` Remainder (modulo) | `__mod__` | `a % b` |
| `==` Equality | `__eq__` | `a == b` |
| `<` Less Than | `__lt__` | `a < b` |
| `>` Greater Than | `__gt__` | `a > b` |
| `<<` Bitwise Left Shift | `__lshift__` | `a << b` |
| `>>` Bitwise Right Shift | `__rshift__` | `a >> b` |
| `&` Bitwise AND | `__and__` | `a & b` |
| `\|` Bitwise OR | `__or__` | `a \| b` |
| `^` Bitwise XOR | `__xor__` | `a ^ b` |
| `~` Bitwise NOT | `__invert__` | `~a` |
| `len()` | `__len__` | `len(a)` |
| `str()` / `print()` | `__str__` | `print(a)` or `str(a)` |
| `repr()` | `__repr__` | `repr(a)` or when inspecting in the console |
| `bool()` | `__bool__` | `bool(a)` or `if a:` |
| `int()` | `__int__` | `int(a)` |
| `float()` | `__float__` | `float(a)` |

The reason this falls under polymorphism is the same idea as before — the `+` operator means something different depending on what objects are involved. `3 + 4` gives you `7`, `"three " + "four"` gives you `"three four"`, and now `p1 + p2` gives you a new `Point`. Same operator, many forms.

---

## Properties

---

Sometimes you want to **control how an attribute is read or written** — for example, to prevent health from going below zero. That's what properties are for.

A property looks like a plain attribute from the outside, but secretly runs a function when you get or set it.

```python
class Soldier:
    def __init__(self, health):
        self._health = health       # _health is the "private" storage
                                    # the _ prefix is a convention meaning
                                    # "don't touch this directly"

    @property
    def health(self):               # getter — runs when you READ health
        return self._health

    @health.setter
    def health(self, value):        # setter — runs when you WRITE health
        if value < 0:
            self._health = 0        # clamp to 0 instead of going negative
        else:
            self._health = value

aragorn = Soldier(100)
print(aragorn.health)               # 100 (uses getter)

aragorn.health = -50                # uses setter — triggers validation
print(aragorn.health)               # 0 (clamped, not -50)
```

---

## Class & Static Methods

---

Most methods act on a specific object (`self`). But sometimes you need methods that act on the **class itself**, or methods that are just utility functions that don't need access to either.

```python
class Soldier:
    count = 0                       # track how many soldiers exist

    def __init__(self, name):
        self.name = name
        Soldier.count += 1

    @classmethod
    def get_count(cls):
        # cls refers to the class itself (like self refers to the object)
        # useful for accessing or modifying class attributes
        return f"There are {cls.count} soldiers"

    @staticmethod
    def is_valid_damage(damage):
        # no access to the class or instance
        # just a utility function that logically belongs here
        return isinstance(damage, int) and damage > 0

s1 = Soldier("Aragorn")
s2 = Soldier("Boromir")

print(Soldier.get_count())          # There are 2 soldiers
print(Soldier.is_valid_damage(25))  # True
print(Soldier.is_valid_damage(-5))  # False
```

| Decorator | First arg | Use when |
|-----------|-----------|----------|
| *(none)* | `self` — the object | You need to read/write the object's data |
| `@classmethod` | `cls` — the class | You need to read/write class-level data |
| `@staticmethod` | *(none)* | It's a utility that belongs to the class but doesn't need `self` or `cls` |

---

[↑ Back to Index](#index)
