# My-Helper-Functions
This repository is containing functions that I use in Python a lot.

# Important Python Concepts in OOP

1) Classes allow us to group data and functions and make them easy to use. We don't have to use `self` in regular methods(like constructor) but using `self` is a convention. In class methods, `cls` is a convention. Class variables are variables that were shared by all instances of Class and they are the same across all instances. If we want class variables to be modified through instances, use them via self. However, if you don't want class variables to be modified through instances, use them via Employee.class_variable or define a **classmethod**(set_raise_amt) that modifies class variable. **from_string** is an alternative method defined via **classmethod**. staticmethod neither takes an cls argument like classmethod nor self argument like regular method. It is in class because of some kind of relationship with Class. In reality, staticmethod shouldn't acess to class or instance eanywhere in itself.

```classes_intro.py
import datetime

class Employee:
    #raise_amount is a class variable
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        #first,last,pay are instance variables.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@mycompany.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee( {} {} {} )".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    # An alternative constructor via classmethod
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) | (day.weekday() == 6):
            return False
        return True

# Setting instances
emp_1 = Employee('Muhammed','Buyukkinaci',100)
emp_2 = Employee('lorem','ipsum',50)
print(emp_1 + emp_2)# 150 = 100 + 50; sums pays of 2 objects thanks to dunder add method
print(repr(emp_1))#Employee( Muhammed Buyukkinaci 100 )
print(str(emp_1))#Muhammed Buyukkinaci - Muhammed.Buyukkinaci@mycompany.com
print(len(emp_1))#20
print(emp_1.email)# Muhammed.Buyukkinaci@mycompany.com
print(emp_1.fullname())#Muhammed Buyukkinaci
# Raising pay
emp_1.apply_raise()
print(emp_1.pay)#104
# Changing raise_amount class variable and applying this change
Employee.raise_amt = 1.5
emp_1.apply_raise()
print(emp_1.pay)#156
print(emp_2.pay)#50
emp_2.apply_raise()
print(emp_2.pay)#75
# Setting raise_amt class variable to 1.05
Employee.set_raise_amt(1.05)
# Applying this change to existing instance
emp_2.apply_raise()
print(emp_2.pay)#75*1.05 = 78
# An alternative constructor to default constructor
emp_3 = Employee.from_string('Ali-Yilmaz-200')
print(emp_3.first)
# staticmethod
my_date = datetime.date(2016,1,1)
print(Employee.is_workday(my_date))# True

class Developer(Employee):
    raise_amt = 1.1
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def add_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("--->",emp.fullname())


dev_1 = Developer('Ahmet','Yilmaz',120,'Python')
dev_1.apply_raise()
print(dev_1.pay)# 120*1.1 = 132
print(dev_1.prog_lang)#Python

man_1 = Manager('Hasan','Yilmaz',150,[dev_1])
print(man_1.email)#Hasan.Yilmaz@mycompany.com

man_1.print_emps()#---> Ahmet Yilmaz

print(isinstance(man_1,Manager))# True
print(isinstance(man_1,Employee))# True
print(isinstance(man_1,Developer))# False

print(issubclass(Developer,Employee))# True
print(issubclass(Manager,Employee))# True
print(issubclass(Developer,Manager))# False

```

2) Some terms about OOP:

- Inheritance: Using methods and attributes of a parent Class in Child Class

- Encapsulation: Accessing the attribute of a Class only in itself(private) by defining the attributes starting with double underscore __. Single underscore _ used for defining protected attributes in a class. Protected means accesible with the Class and its subclasses. No underscore for public attributes. If we want to see method resolution order or a sub class, run `print(help(Developer)) Every class in Python inherits from builtins.object class. Change in child class doesn't affect parent class.

- Polymorphism: Being available to send different inputs to a method or a function like Python's built-in len function.

- Method Overriding: Rewriting a method inherited from a parent class in the Child class.

- Method Overloading: Calling same method with different number of parameters like we did in C#. Two methods can't have the same name in Python. Not possible in Python.

3) Double underscores is called as dunder. \__init__ is a special method. \__repr__ and \__str__. These 2 special methods allow us to change how our objects are printed and displayed. len is a special method too, which runs a dunder method named \__len__ .

```
print(1+2)#
print(int.__add__(1,2))#3
print(str.__add__('a','b')) # 'ab'
print(len('test'))#4
print('test'.__len__())
```

4) The goal of repr is to be unambiguous. The goal of str is to be readable. repr is mostly used in debugging.

![property](./images/010.png)

5)  What does `if __name__ == '__main__'` mean? Whenever Python runs a file, it first goes through before even runs any code, it sets a few special variables. \__name__ is one of these special variables. `if __name__ == '__main__'` checks whether a file in being run directly or imported from a different module. It returns True if directly run from script and returns False if it called from another script. The reason why we use our codes in main function in first_module.py is to make it importable in another script.


```first_module.py
#first_module.py

print("This will always be run")

def main():
    print("First module's name: {}".format(__name__))

if __name__ == '__main__':
    print("Runs directly")
    main()
else:
    print("Run from import")

```

```second_module.py
import first_module
print("Second module's name: {}".format(__name__))
```


6) property usage in Python classes. property is making a method as an attribute of a Class. It is a decorator. peperty decorator allows us to define method but we can access it like an attribute.

```property_usage.py
# Property Decorator
class Personnel:
    def __init__(self,first,last,pay):
        #first,last,pay are instance variables.
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@mycompany.com'
    def fullname(self):
        return f'{self.first} {self.last}'

per_1 = Employee('John','Smith',100)
per_1.first = 'Jim'
print(per_1.first)#Jim
print(per_1.email)#John.Smith@mycompany.com
print(per_1.fullname())#Jim Smith

class Worker:
    def __init__(self,first,last,pay):
        #first,last,pay are instance variables.
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@mycompany.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name !")
        self.first = None
        self.last = None

wor_1 = Worker('John','Smith',100)
wor_1.first = 'Jim'
print(wor_1.first)#Jim
print(wor_1.email)#Jim.Smith@mycompany.com
print(wor_1.fullname)#Jim Smith

wor_1.fullname = "Muhammed Büyükkınacı"
print(wor_1.first)#Muhammed
print(wor_1.email)#Muhammed.Büyükkınacı@mycompany.com
print(wor_1.fullname)#Muhammed Büyükkınacı

del wor_1.fullname# delete name !
```

![property](./images/000.png)

7) self is a conventional name in Python classes, not a magical keyword. It could be s or me or whatever we name. 

8) To check if a variable has a numeric type of Float, integer, Decimal etc; use isinstance.

```filename.py
import numbers
isinstance(variable_name,numbers.Number)
```

9) Always try to make code DRY(don't repeat yourself)

10) String interpolations should be used instead of string concatenation. String interpolation is less prone to errors. If we are repeating placeholders, we can assign indexes to them. WE can make the same operation like zfill in formatting strings via `:`.

```string_interpolation.py

a = 2
b = 'Muhammed'

# The former one is string concatenation
my_string = 'I am ' + b ' and I have ' + str(b) + 'computers'

# The latter is string interpolation
my_string = 'I am {} and I have {} computers'.format(b,a)

# Use multiple same placeholders via assigning placeholders
my_string = "I am {0} and I am {1} years old. {1} years old is a critical age in human life.".format('Muhammed',28)

# Dict usage in string interpolation
mydict = {'name':'Muhammed','age':28}
my_string = "I am {0[name]} and I am {0[age]} years old. {0[age]} years old is a critical age in human life.".format(mydict)

# List usage in string interpolation
mydict = ['Muhammed',28]
my_string = "I am {0[0]} and I am {0[1]} years old. {0[1]} years old is a critical age in human life.".format(mydict)


```

11) Idempotency is a programming term meaning that calling something(an HTTP word, python function etc.) once is the same as calling it multiple times. GET, PUT, DELELTE are idempotent HTTP words. POST isn't a idempotent HTTP word.

```idempotent.py
def func_not_idempotent(x):
    return x + 20

# Not idempotent
#func_not_idempotent(func_not_idempotent(10)) != func_not_idempotent(10)

def func_idempotent(x):
    return abs(x)

# Idempotent
func_idempotent(-10) == func_idempotent(func_idempotent(-10)) == func_idempotent(func_idempotent(func_idempotent(-10)))
```

12) namedtuple is more readable. Its is also immutable. It is an alternative to Python dictionaries but less prone to typing errors.

```namedtuple.py
from collections import namedtuple

Color = namedtuple('Color',['red','green','blue'])

white = Color(255,255,255)
black = Color(0,0,0)
gray = Color(red = 128, green = 128, blue = 128)

print(f"red index of white = {white.red} ")
print(f"green index of black = {black.green} ")
print(f"blue index of gray = {gray.blue} ")

```

13) `id` is showing us the location of an object on memory. Assigning a different value to an existing object is creating it from scracth and therefore it is slow.
```python_id.py
a = 'Ozan'
a = 'Ozan'
print(f"{a}; its location on memory = {id(a)}")
a = 'Burak'
print(f"{a}; its location on memory = {id(a)}")
# The last print prompts error.
a[0] = 'D'
print(f"{a}; its location on memory = {id(a)}")
#Ozan; its location on memory = 140241796670896
#Burak; its location on memory = 140241796670832
```

14)  String objects are immutable. However, list is mutable. Preferring mutable objects(list) instead of immutable objects is more logical in concatenating lots of strings because mutable objects aren't creating new objects each time like immutable objects(String etc.) did.

```mutable_vs_immutable.py
a = 'Burak'
print(f"{a}; its location on memory = {id(a)}")
# The below print prompts error.
a[0] = 'D'
print(f"{a}; its location on memory = {id(a)}")
```

15) else statement in loops(for or while) should be considered as no-break. it is executed if for loop runs smoothly.

```for_else.py
a = [1,2,3,4,5]
for i in a:
    print(i)
    if i == 3:
        break
else:
    print("While else print executed at the end because no break happened")
```

```while_else.py
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("While else print executed at the end because no break happened")
```

```practical_loop_else.py
def index_finder(passed_list,searched_word):
    for index, i in enumerate(passed_list):
        if searched_word == i:
            break
    else:
        return -1
    return index

print(index_finder(['a','b','c','d','e'],'b'))#prints 1
print(index_finder(['a','b','c','d','e'],'f'))#prints -1
```

16) Python generator don't hold entire results in memory therefore it improves performance. Holding millions of records in a generator is more performant than holding millions of records in list.

``` python_generator.py

nums_list_comp = [pow(i,3) for i in [3,4,5]]
print(nums_list_comp)
#[27,64,125]

nums_generators_like_list_comp = (pow(i,3) for i in [3,4,5])
print(nums_generators_like_list_comp)
#<generator object <genexpr> at 0x7fa53c98a650>
print(next(nums_generators_like_list_comp))
# 27
print(next(nums_generators_like_list_comp))
# 64
print(next(nums_generators_like_list_comp))
# 125

def legacy_solution(nums):
    return_list = []
    for i in nums:
        return_list.append(pow(i,3))
    return return_list

nums_legacy = legacy_solution([3,4,5])
print(nums_legacy)
#[27,64,125]

def generator_solution(nums):
    for i in nums:
        yield (pow(i,3))

nums_generators = generator_solution([3,4,5])
print(nums_generators)
#<generator object generator_solution at 0x7f9e1c3c2650>
for i in nums_generators:
    print(i)
#27
#64
#125

```

17) map&lambda and filter&lambda functions in python3 are evaluated lazily. Prefer list comprehensions over map&lambda and filter&lambda pairs. asteriks(*) is used to show map or filter

```prefer_lc.py
nums = [1,2,3]
#Take squares in list comprehensions
print([n**2 for n in nums])#prints: [1, 4, 9]
# Same operation using map and lambda
mapped = map(lambda n: n*n, nums)
print(mapped)#prints: <map object at 0x7f4b6bb5bbb0>
print(*mapped)# prints 1,4,9

filtered = filter(lambda n: n%2==1, nums)
print(filtered)#prints: <map object at 0x7f4b6bb5bbb0>
print(*filtered)# prints 1,3
```

18) Memoization is a programming term meaning caching results of a computationally expensive operation recurring more than once instead of re-computation. The code below runs in 2 seconds thanks to memoization instead of 4 seconds.

```memoization.py
import time
square_dict={}
def take_squares(num):
    if num in square_dict:
        return square_dict[num]
    print(f"Computing results for {num}")
    time.sleep(1)
    result = num * num
    square_dict[num] = result
    return result

result = take_squares(4)
print(result)
result =take_squares(10)
print(result)
result =take_squares(4)
print(result)
result =take_squares(10)
print(result)

```

19) Slicing in list is programmed in the format of `list_name[start:end:step]`. The default step is 1.

```slicing.py
my_list = [0,1,2,3,4,5,6,7,8,9]
print( my_list[2:-1:1] )# prints [2, 4, 6, 8]
#Reverse with respect to start, end and step
print( my_list[-1:-8:-2] )#[9, 7, 5, 3]
# Reverse all list
print(mylist[::-1])
# Reverse the string
my_string = "a string is here"
print(my_string[::-1]) #ereh si gnirts a

```

20) In Python, to list all builtin attributes or exceptions or errors, run `print(dir(locals()['__builtins__']))` .

21) `try`, `except`, `else` and `finally` are keywords in exceptions. THere may be multiple except keyword in error handling. Put the specific exceptions in above excepts and put general ones in below excepts. else runs if try doesn't raise an exception. `finally` is run in every condition. To manually raise an exception, use `raise Exception`

```exception01.py

# Definin a custom exception
class MyDefinedException(Exception):
    pass

a33 = 20
try:
    a = a33
    file = open('.gitignore')
    if a == a33:
        raise MyDefinedException
except NameError as e:
    print("Name error occured")
    print(e)
except FileNotFoundError as e:
    print("an error occurred")
    print(e)
except MyDefinedException as e:
    print("My defined exception runs")
except Exception as e:
    print("another exception except above ones happened")
    print(e)
else:
    print("no exception happened")
finally:
    print("finally prins run in every condition")

#My defined exception runs
#finally prins run in every condition
```

```exception02.py

a33 = 20
try:
    a = a33
    file = open('.gitignore')
except NameError as e:
    print("Name error occured")
    print(e)
except FileNotFoundError as e:
    print("an error occurred")
    print(e)
except Exception as e:
    print("another exception except above ones happened")
    print(e)
else:
    print("no exception happened")
finally:
    print("finally prins run in every condition")

#no exception happened
#finally prins run in every condition

```

22) Being Pythonic means following conventions and coding styles of Python in order to write clean and readable code. 2 common concepts to become Pythonic:
Duck Typing and Easier to ask forgiveness than permission(EAFP).

23) **Duck Typing** is that the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Duck typing is implemented in Dynamic languages like Python, Perl, JS. Duck typing emphasizes what the object really can do rather than what the object is.

```duck_typing.py
class Duck:
    def fly(self):
        print("Duck is flying")
    def quack(self):
        print("Duck is quacking")
class Bear:
    def fly(self):
        print("Bear is flying")
    def quack(self):
        print("Bear is quacking")
def fly_and_quack(thing):
    if isinstance(thing,Duck):
        thing.fly()
        thing.quack()

def duck_typed_fly_and_quack(thing):
    thing.fly()
    thing.quack()

duck = Duck()
bear = Bear()

print("No duck typing")
fly_and_quack(duck)
fly_and_quack(bear)
# outputs below:
#No duck typing
#Duck is flying
#Duck is quacking
# outputs below:
print("Duck typing")
duck_typed_fly_and_quack(duck)
duck_typed_fly_and_quack(bear)

#Duck typing
#Duck is flying
#Duck is quacking
#Bear is flying
#Bear is quacking

```


24) **LBYL**(Look Before You Leap) and **EAFP**(Easier to ask forgiveness than permission) are 2 terms in Programming. Python is EAFP. LBYL is using lots of if-else statements. EAFP suggests using try/except blocks instead of multiple checks via if-else statements. If your code hass less exceptions, EAFP is faster than LBYL because we access the object once.

```lbyl_vs_eafp.py

person1 = {'name':'Muhammed','age':28, 'job':'Data Scientist'}
person2 = {'name':'Muhammed','age':28}

def lbyl(person):
    # LBYL
    if ('name' in person) and ('age' in person) and ('job' in person):
        print( "I am {}, I am {} years old, I am working as a {} ".format(person['name'],person['age'],person['job']) )
    else:
        print("there are some missing keysin LBYL")

def eafp(person):
    try:
        print( "I am {}, I am {} years old, I am working as a {} ".format(person['name'],person['age'],person['job']) )
    except KeyError as e:
        print("there are some missing keys in EAFP")

lbyl(person1)# I am Muhammed, I am 28 years old, I am working as a Data Scientist 
eafp(person1)# I am Muhammed, I am 28 years old, I am working as a Data Scientist 

lbyl(person2)# there are some missing keysin LBYL
eafp(person2)# there are some missing keys in EAFP
```

25) **First class functions** allows us to treat functions like any other object. It is an important concept which is about passing function as arguments or assigning them to variables or returning functions as a result in functions etc. If a function takes a function as argument or returns a function as the result or the function is assigned to another variable, it is called high-order function.

```first_class_functions.py
# 1) Assign a function to a variable
def square(x):
    return x * x
f = square
print(f(5))
# 2) Pass functions as arguments
def cube(x):
    return x * x *x
def mapper(func,arguments):
    result_list = []
    for i in arguments:
        result_list.append(func(i))
    return result_list
results = mapper(cube,[1,2,3])
print(results)# [1, 8, 27]
# 3) Returns functions as results. This way is similar to decorators and used in logging.
def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag,msg))
    return wrap_text
print_h1 = html_tag('h1')
print_h1('Test')#<h1>Test</h1>
print_h1('Another Test')#<h1>Another Test</h1>
print_p = html_tag('p')
print_p('Test')#<p>Test</p>

```

26) A Closure is an inner function that remembers and has access to variables in the local scope in which it was created even if the outer function has finished executing. A closure closes over the free variables from their environment. Understanding closures helps to comprehend decorators.

```closure.py
# Example 1:
def outer_function():
    message = "Muhammed"
    def inner_function():
        return message
    return inner_function

my_variable = outer_function()
print(my_variable)#<function outer_function.<locals>.inner_function at 0x7f66efe79fc0>
print(my_variable())#Muhammed
# Example 2:
def outer_function(msg):
    #message is a free variable.
    message = msg
    def inner_function():
        print( message)
    return inner_function

print_hi = outer_function('Hi')
print_hello = outer_function('Hello')
print_hi()# Hi,
print_hello()# Hello
# Example 3:
import logging
logging.basicConfig(filename='logs/closure.log',level=logging.INFO)

def log_outer_function(function):
    def log_inner_function(*args):
        logging.info("The function named {} is executed {}".format(function.__name__,args))
        print(function(*args))
    return log_inner_function

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

add_logger = log_outer_function(add)
subtract_logger = log_outer_function(subtract)
add_logger(3,3)# 6
add_logger(5,10) # 15
subtract_logger(10,3) # 7
subtract_logger(60,20) # 40

#INFO:root:The function named add is executed (3, 3)
#INFO:root:The function named add is executed (5, 10)
#INFO:root:The function named subtract is executed (10, 3)
#INFO:root:The function named subtract is executed (60, 20)
```

27) args is recognized as positional arguments and kwargs are recognized as keyword arguments.

28) Decorator is similar to first class functions and closures. Decorator is a function takes a function as an argument and adds some kind of functionality and returns another function. All of these without altering source code of the original function that we passed in. We can pass positional arguments and keyword arguments of input functions to decorators via `*args, **kwargs`. Some people tend to use decorators as classes rather than functions. Decorators are commonly used in Python in the task of Logging. Decorators are also used for timing how long functions run. Decarators enable us to maintain our edit functionality in one location. We can stack decorators on top of each other.

```decorator_simple.py
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function
def display():
    print("display ran")
decorated_display = decorator_function(display)
decorated_display()
```

```decorator_args_kwargs.py
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f"wrapper function named {original_function.__name__} ran")
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display ran")
display()

@decorator_function
def display_info(name,age):
    print("display info function run with arguments {} {}".format(name,age))
display_info('Muhammed',28)
```

```decorator_as_class.py
class Decorator_Class(object):
    def __init__(self,original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__} ran")
        return self.original_function(*args,**kwargs)
@Decorator_Class
def display_info(name,age):
    print("display info function run with arguments {} {}".format(name,age))
display_info('Muhammed',28)
```

```decorator_logging.py
def my_logger(orig_function):
    import logging
    logging.basicConfig(filename = f'logs/{orig_function.__name__}.log',level=logging.INFO)
    def wrapper(*args,**kwargs):
        logging.info(f"run with args : {args} and kwargs {kwargs}")
        return orig_function(*args,**kwargs)
    return wrapper

@my_logger
def display_info(name,age):
    print("display info function run with arguments {} {}".format(name,age))

display_info('Muhammed',28)
```

```decorator_timer.py
import time
def my_timer(orig_function):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_function(*args,**kwargs)
        t2 = time.time()
        print(f"{orig_function.__name__} ran in {t2 - t1} seconds")

        return result
    return wrapper

@my_timer
def display_info(name,age):
    time.sleep(1.0)
    print("display info function run with arguments {} {}".format(name,age))

display_info('Muhammed',28)
```

29) If we stack 2 decorators for one function, the inner decorator(my_timer) returns a wrapper function and that wrapper function gets fed into the outer decorator(my_logger). This may result in unexpected names in logfiles or in prints. We can decorate decorators via functools.

```decorating_multiple_decorators.py
from functools import wraps
import time
import logging

def my_logger(orig_function):
    logging.basicConfig(filename = f'logs/{orig_function.__name__}.log',level=logging.INFO)
    @wraps(orig_function)
    def wrapper(*args,**kwargs):
        logging.info(f"run with args : {args} and kwargs {kwargs}")
        return orig_function(*args,**kwargs)
    return wrapper

def my_timer(orig_function):
    @wraps(orig_function)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig_function(*args,**kwargs)
        t2 = time.time()
        print(f"{orig_function.__name__} ran in {t2 - t1} seconds")
        return result
    return wrapper
    
@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1.0)
    print("display info function run with arguments {} {}".format(name,age))

display_info('Muhammed',28)
# == my_logger(my_timer(display_info()))
```

30) We can define decorators with arguments via decorating a decorator.

```decorator_with_arguments.py

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args,**kwargs):
            print(prefix," Executed before", original_function.__name__)
            result = original_function(*args,**kwargs)
            print(prefix," Executed after", original_function.__name__)
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('LOG:')
def display_info(name,age):
    print("display info ran with arguments ( {}, {} ) ".format(name,age))

display_info('Muhammed',20)
display_info('Muhammed',30)
#LOG:  Executed before display_info
#display info ran with arguments ( Muhammed, 20 ) 
#LOG:  Executed after display_info
#LOG:  Executed before display_info
#display info ran with arguments ( Muhammed, 30 ) 
#LOG:  Executed after display_info
```

31) Some commonly used os module functions

```os_module.py
# To create a directory in a nested way or one directory
os.makedirs('path_to_out_directory/path_to_inner_directroy')
# To remove a directory
os.removedirs('path_to_out_directory/path_to_inner_directroy')
# Get some info about a file
os.stat('demo.txt')
#os.stat_result(st_mode=33204, st_ino=13502420, st_dev=66306, st_nlink=1, st_uid=1000, st_gid=1000, st_size=3090, st_atime=1653933450, st_mtime=1653412360, st_ctime=1653412360)
# To see files and directories in each directory and sub directories, it returns a tuple of
os.walk(PATH_TO_DISCOVER)
#To get the value of an environment variable
os.environ.get('HOME')
# To get the basename of a file, not the directory
os.path.basename('/home/muhammed/temp.txt') # temp.txt
# To get the dirname of file, not the base name
os.path.dirname('/home/muhammed/temp.txt') # /home/muhammed
# To get dirname and basename in a tuple of dirname,basename
os.path.split('/home/muhammed/temp.txt') # ('/home/muhammed', 'temp.txt')
# To check a file exists or not, returning True or False
os.path.exists('/home/muhammed/temp.txt') # ('/home/muhammed', 'temp.txt')
# To check something whether it is directory or not
os.path.isdir('/home/muhammed/temp.txt') # False or False
# To check something whether it is file or not
os.path.isfile('/home/muhammed/temp.txt') # True or False
# To split filename and extension
os.path.splitext('/home/muhammed/temp.txt')#('/home/muhammed/temp', '.txt')
```

32) open command can allow us to make these 4 operations: reading(r), writing(w), appending(a), reading & writing(r+). The default is reading. When we open a file, it is required to close it explicitly. This way(no context managers) isn't recommended. If we open a file via **open** and **as**, we don't have to close it explicitly.

```open_command.py
f = open('.gitignore','r')
print(f.name)# .gitignore
print(f.mode)# r
f.close()

with open('.gitignore') as f:
    f_contents = f.read()
    print(f_contents)

with open('.gitignore') as f:
    f_contents = f.read()
    f_contents = f.readline()# to read 1 line
    f_contents = f.readlines()# to read files in a list
```

33) We shouldn't give mutable arguments to functions by default. That means that giving a list or dictionary as an argument by default might be dangerous. This is why we pass None as default argument.

34) Python, there are 5 data types such as dates, times, datetimes, timedeltas and timezones. Naive dates and times don't have enough information to determine things like timezone. Timedeltas are simply differences between 2 dates or times. If we subtract one date from another date or one time from another time, the result is timedelta. We can access date and time from a datetime object. Pytz is a library to deal with timezones, recommended by Python official documentation. It is recommended to work with UTC in timezones.

```tims_diffs.py
import datetime
import pytz
## Date
# years, months and days
d = datetime.date(2016,5,25)
# To create a date object of today
tday = datetime.date.today()#2022-06-04, saturday
print(tday.year)# 2022
print(tday.weekday())# 5 
print(tday.isoweekday()) # 6
## Timedelta
tdelta = datetime.timedelta(days =7)
print(tday + tdelta)#2022-06-11
## Difference between 2 dates
bday = datetime.date(2016,9,19)
till_bday = bday - tday
print(till_bday)#-2084 days, 0:00:00
## Time; 
# hours minutes, seconds, microseconds
t = datetime.time(21,30,33,199999)
print(t.hour) # 21
## Datetime
# Datetime is Merge of date and time objects
dt = datetime.datetime(2016,1,3,12,30,45,199199)
print(dt.date())#2016-01-03
print(dt.time())#12:30:45.199199
# Subtracting timedelta object from datetime object
tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)#2016-01-10 12:30:45.199199
# Timezone awared
dt_today = datetime.datetime.today()# timezone is none by default
dt_now = datetime.datetime.now()# we can pass timezone as parameter
dt_utcnow = datetime.datetime.utcnow()# timezone aware datetime
print(dt_today)
print(dt_now)
print(dt_utcnow)
# PYTZ
tz_aware = datetime.datetime(2016,7,27,12,39,45,tzinfo=pytz.UTC)
print(tz_aware)
# Current UTC time
dt_machinenow = datetime.datetime.now()
print(dt_machinenow)#2022-06-05 11:48:52.022640
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)# Turkey is UTC + 3. UTC is 3 hours behind.
print(dt_utcnow)#2022-06-05 08:48:52.022652+00:00
# Possible Timezones,
for tz in pytz.all_timezones[:2]:
    print(tz)
# Convert this to different Timezone, US/Eastern
dt_different = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_different)#2022-06-05 04:48:52.022652-04:00
# Convert dateitme object to string
print(dt_utcnow.strftime('%B %d, %Y'))#June 05, 2022
# Convert string to datetime
time_string = "June 05, 2022"
converted_to_dt = datetime.datetime.strptime(time_string,'%B %d, %Y')
print(converted_to_dt)#2022-06-05 00:00:00
```

35) Variable Scope is composed of 4 components: LEGB (Local - Enclosing - Global - Built-in ). **Local** variables are variables in which defined in a function. **Enclosing** variables are variables in local scope of enclosing functions. **Global** are variables defined at the top level of a module, explicitly declared global. **Builtins** are pre-assigned variables. Python checks a variable in LEGB order. Using `global` statement isn't mostly recommended. `nonlocal` is a statement similar to `global`, but used in inner function to do what `global` statement does.

```scope.py
# Setting a local variable as global. global keyword makes a local variable change global
x = 'global x'
def test():
    global x
    x = 'local x'
    print(x)
print(x)#global x
test()#local x
print(x)#local x
# Builtin names pre-assigned ones.
import builtins
print(dir(builtins))
# Don't override builtin functions
# def min():
#     pass
m = min([4,2,1])
print(m)
# Enclosing has to do with nested functions. It is similar to local & global scopes

def outer():
    # Local to our outer function
    x = 'outer x'
    def inner():
        # Local to inner function
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()# The output is below:
# inner x
# outer x

def outer():
    x = 'outer x'
    def inner():
        print(x)
    inner()
    print(x)

outer()# The output is below:
#outer x
#outer x

x = 'global x'
def outer():
    def inner():
        print(x)
    inner()
    print(x)

outer()# The output is below:
#global x
#global x
```

36) Python **random** module shouldn't be used for security purposes and cryptography and Python suggests to use **secrets** module for these aims.

```random_module.py
import random
# Get a random number between 0 and 1; not used frequently
value = random.random()
print(value)# between [0,1)
# Uniform distribution; not used frequently
value = random.uniform(1,10)
print(value)# between [1,10)
# Random integers; used frequently
value = random.randint(1,6)
print(value)# between [1,6]
# To pick one random value from a list
cars = ['BMW','Mercedes','Audi','Porsche','Opel','VW','Skoda','Seat']
value = random.choice(cars)
print(value)#'Porsche'
# To pick 2 random values from a list; multiple elements may occur
results = random.choices(cars,k = 5)
print(results)#['Mercedes', 'Mercedes', 'BMW', 'Mercedes', 'Audi']
# To assign weights to elements of a list
results = random.choices(cars,k = 5,weights=[10,20,30,40,5,5,5,5])
print(results)#['Porsche', 'BMW', 'Mercedes', 'Porsche', 'Porsche']
# Not recurring samples
hand = random.sample(cars,k = 5)
print(hand)#['BMW', 'VW', 'Opel', 'Seat', 'Porsche']
```

37) In Python 2, xrange is working like a generator and range is loading all results into memory and returning all results once. In dictionaries, iteritems works like a generator and items works like lists.

38) [reveal.js](https://revealjs.com/) is a JS library which provides slides on browser.

39) Fluent Python is a book by Luciano Ramalho, which is an advanced level Python book.

40) RegEx allow us to search specific text and replace it instead of explicit search like we did in word or vscode.

![regex1](./images/011.png)

![regex2](./images/012.png)

41) Regex in Python. `.` is a special character in RegEx. If we want to search `.` in text, we should escape it via backward slash(\). Meta characters should be escaped via `\` if you want to search them. Capital letters basicly negate whatever the lowercase version is (\d means digit and \D means not a digit). \b means word boundary and \B means not a word boundary. ^ means beginning of a string and $ means end of a string `[]` is character set that takes relevant characters inside and corresponding to one character in search pattern. `-` in [] means range (boundaries are inclusive)**[1-5]**. `^` negates the set and matches everything that isn't in that character set [^a-zA-Z]. `|` operator is meaning or and () are used to group **(Mr|Mrs|Ms)**. For some common usages like e-mail addresses, there are some patterns available online. Reading regex's of other people is harder than writing. To make the regex case insensitive,
add **re.IGNORECASE** to **re.compile** method

```regex.py
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
#<re.Match object; span=(53, 56), match='abc'>
#<re.Match object; span=(58, 61), match='abc'>

```

42) Regex expression examples are below:

```regex.py
# Data 1: 
# 321-555-4321
# 123.555.1234
# Regex of Data 1:
# re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# Data 2:
# 800-555-1234
# 900-555-1234
# re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# Data 3(cat,mat,pat included and bat excluded):
# cat
# mat
# pat
# bat
re.compile(r'[^b]at')

# Data 4, {3} is excluded: 
# 321-555-4321
# 123.555.1234
re.compile(r'\d{3}.\d{3}.\d{3}')

# Data 5
# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
re.compile(r'(Mr|Ms|Mrs)\.\s[A-Z]\w*')

# Data 6
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# Data 7
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
#grouping into domain name, extension etc.
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# Substituting
subbed_urls = pattern.sub(r'\2\3',urls)

## pattern.finditer alternatives
# sub
# pattern.findall(text_to_search)# return list of all matches
# pattern.match() # not returning an iterable, returns the first match
# pattern.search() #

```

43) Web scraping with Beautiful Soup. Install it via `pip install beautifulsoup4` . Beautiful soup recommends lxml parser via `pip install lxml`. There is another parser named **html5lib**. Finally, install requests library via `pip install requests`. We should call `prettify` method of BeautifulSoup object. We can access the information in BeautifulSoup object as the attributes. **find** method returns the first match in html object. **find_all** method returns all matches as a list. If we want to get attribute(src) of a tag(iframe), we can access it like a dictionary  `article.find('iframe',class_ = 'youtube-player')['src']`.

```web_scrape.py
from bs4 import BeautifulSoup
import requests
import csv

### Working with a local html file

## Loading local html file via lxml parser
with open('simple.html','r') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

## Not indented object
print(soup)
## Seeming human readable
print(soup.prettify())

## title returns first title object in page
match = soup.title
print(match)

#<title>Test - A Sample Website</title>
text = soup.title.text
print(text)
#Test - A Sample Website

## Filter divs whose class = footer
match = soup.find('div',class_ = 'footer')
print(match)
#<div class="footer">
#<p>Footer Information1</p>
#</div>


article = soup.find('div',class_ = 'article')
headline = article.h2.a.text
print(headline)
#Article 1 Headline
summary = article.p.text
print(summary)
#This is a summary of article 1


## Loop through all divs having article class
for article in soup.find_all('div',class_ = 'article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

#Article 1 Headline
#This is a summary of article 1
#Article 2 Headline
#This is a summary of article 2

### Working with urls
source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

article = soup.find('article')
headline = article.h2.a.text
print(headline)
#Python Tutorial: Zip Files – Creating and Extracting Zip Archives

## first div whoxse class = entry-content
summary = article.find('div',class_ = 'entry-content').p.text
print(summary)
#In this video, we will be learning how to create and extract zip archives.
#We will start by using the zipfile module, and then we will see how to do 
#this using the shutil module. We will learn how to do this with single 
#files and directories, as well as learning how to use gzip as well. 
#Let’s get started…


vid_src = article.find('iframe',class_ = 'youtube-player')['src']
print(vid_src)
#https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)
#z0gguhEmWiY
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
#https://youtube.com/watch?v=z0gguhEmWiY


## List links of all videos
source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source,'lxml')
# Create a csv file to pass data in
csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div',class_ = 'entry-content').p.text
    try:
        vid_src = article.find('iframe',class_ = 'youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    # Appending row
    csv_writer.writerow([headline,summary,yt_link])
# Closing because we didn't open the file with context managers.
csv_file.close()
```

44) JSON means Javascript object notation. json is pre-installed library in Python. We should treat json files like getting values of Python dictionaries via keys.

![json_conversion](./images/013.png)

```json_usage.py

import json
## Convert json to Python object
json_string = """
{
    "people":[
        {
            "name": "Muhammed",
            "age": 28
        },
        {
            "name": "Hasan",
            "age": 29
        }
    ]
}
"""
data = json.loads(json_string)
print(type(data))#<class 'dict'>
print(type(data['people']))#<class 'list'>

for person in data['people']:
    print(person)

#{'name': 'Muhammed', 'age': 28}
#{'name': 'Hasan', 'age': 29}

# Convert Python object to Json
new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)

#{
#  "people": [
#    {
#      "age": 28,
#      "name": "Muhammed"
#    },
#    {
#      "age": 29,
#      "name": "Hasan"
#    }
#  ]
#}

# Load a .json file
with open('states.json') as f:
    data_loaded = json.load(f)

for row in data_loaded['people']:
    print(row)

#{'name': 'Faruk', 'age': 38}
#{'name': 'Tarık', 'age': 48}

# Dump an object into json file

with open('dumped_states.json','w') as f:
    json.dump(data_loaded,f,indent=2)



# A real world example from Yahoo Finance API

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

print(len(data['list']['resources']))

```

45) Pillow is a library to manipulate images. Pillow is a fork of the Python Imaging Library (PIL). resize method resizes image with respect to desired sizes.. thumbnail method resizes image without changing aspect ratio and not enlarging image(only reducing size by keeping aspect ratio).

```pillow_intro.py
from PIL import Image, ImageFilter
import os

size_300 = (100,100)

image1 = Image.open("mbk.jpg")
image1.show()
# Saving image
image1.save('mbk.png')

# Saving image as png
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn,fext = os.path.splitext(f)
        i.save(f"pngs/{fn}.png")

# Resize images
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn,fext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save(f"300/{fn}_300{fext}")

# Rotate image
image1.rotate(90).save('mbk_rotated.jpg')
# Convert to black and white
image1.convert(mode='L').save('mbk_black_white.jpg')
# Blur image, 15 is radius of blurring effect
image1.filter(ImageFilter.GaussianBlur(15)).save('mbk_blurred.jpg')
```

46) **Context Managers** allow us to properly manage resources so that we can specify exacyly what we want to set up and tear down when working with certain objects. We no longer have to close down opened files within context managers. If an error is thrown, it is still get closed properly. This is why context managers are super useful. Context managers can be used to read a file, connect to a database. There are a couple of ways to write our custom context managers. We can use them via creating classes or creating functions via decorators. Using context managers via functions is mostly preferred way. It is used in opening and closing DB connections; acquiring and releasing locks etc.

```context_managers.py
# Naive way to open a file
with open('sample.txt') as f:
    f.write('Lorem ipsum etc')

# Context managers via Classes
class Open_File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        pass
    
    # For set up purpose
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    # For tear down purpose
    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()

# f is the return value of __enter__ method
# __exit__ is executed when context manager ended, that why f.close return True
with Open_File('sample.txt','w') as f:
    f.write('Testing')

print(f.closed)# True
# Context managers via functions
from contextlib import contextmanager


@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        # Tear down equivalent
        f.close()

with open_file('sample.txt','w') as f:
    f.write('Lorem ipsum')

print(f.closed)

# Practical Usage of Context Manafers
#Legacy code
import os
cwd = os.getcwd()
# Setup
os.chdir('images/')
print(os.listdir())
#['012.png', '008.png', '013.png', '000.png', '009.png', '002.png', '011.png', 
# '003.png', '010.png', '004.png', '006.png', '005.png', '007.png', '001.png']
# Tear down
os.chdir(cwd)

cwd = os.getcwd()
# Setup
os.chdir('logs/')
print(os.listdir())
#['display_info.log', 'app.log', 'basic.log', 'app2.log', 'closure.log']
# Tear down
os.chdir(cwd)

# Context Manager Solution
import os
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        # we aren't working with variables, therefore yield returns Nothing
        yield
    finally:
        os.chdir(cwd)

# Not having as f because yield returns nothing.
with change_dir('images/'):
    print(os.listdir())

#['012.png', '008.png', '013.png', '000.png', '009.png', '002.png', '011.png', 
# '003.png', '010.png', '004.png', '006.png', '005.png', '007.png', '001.png']

with change_dir('logs/'):
    print(os.listdir())

#['display_info.log', 'app.log', 'basic.log', 'app2.log', 'closure.log']
```



# Python Logging

[Video Link 1](https://www.youtube.com/watch?v=-ARI4Cz-awo)

[Video Link 2](https://www.youtube.com/watch?v=jxmzY9soFXg)

1) Python logging becomes more meaningful when the project gets bigger.

2) Logging levels allow us to specify exactly what we want to log by separating these into 5 different categories.

- DEBUG: Detailed info, typicaly of interest when diagnosing problems.

- INFO: Confirmation that things are going well

- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future("eg, disk space low"). The software is still working as expected.

- ERROR: Due to a more serious problem, the software hasn't been able to perform some function.

- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

3) The default level for logging is set to Warning. If logging is set to warning, it will show warning, error and critical loggings. If it is info, it will show info,warning, error and critical.

![logging_levels](./images/001.png)

4) Python logging is similar to print statement in terms of functionality. An example code for logging is as follows:

```logging_similar.py
import logging
def add(x,y):
    return x + y

a = 10
b = 5

add_result = add(10,5)

logging.debug("{} + {} = {}".format( a, b, add_result ) )

```

5) To change logging level

```change_log_level.py
import logging
#logging.DEBUG is different than logging.debug. logging.DEBUG is an integer in the background.
logging.basicConfig(level=logging.DEBUG)
```

6) Log files are great way to capture information because it allows to see our logged information over time in one place.

7) Use log files instead of printing on console.

8) Store your logs in a log file like I did below

```store_log.py
import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)
```

9) We can format log lines by specifying in configuration.

```format_log_str.py
import logging
# Log in this format: time:loglevel:message
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
```

10) You can take a look at python log attributes from [here](https://docs.python.org/3/library/logging.html#logrecord-attributes).

11) Name like root can be specified in format of logging.basicConfig like below:

```change_config.py
import logging
# Log in this format: time:loglevel:message
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
```

12) Since we haven't specified a specific logger, we are working with root logger. Working with root logger isn't the best option. If we are importing file01.py from file02.py, logger configuration of file01.py will be valid in file02.py. Logger configuration of file02 will be invalid.

13)  Despite we define a logger using logging.getLogger, we are still configuring using logging.basicConfig()

```file01.py
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
logger.info('What will be logged here')

```

14) We can split parameters of logging.basicConfig into different lines. If file01.py run directly, the name is __main__. If we import file01.py from file02.py, the name in lines of log file is file01.

15) We are adding formatting to file handler, not to the logger. Logging level should be attached to logger directly.

16) If we want to keep only errors in log file, we can make this by specifying `file_handler.setLevel(logging.ERROR)`.

```file01.py

# Importing module
import logging
# Creating a logger object
logger = logging.getLogger(__name__)
# Setting logging level in the script as INFO
logger.setLevel(logging.INFO)

# Defining a log formatter
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
# Defining a file handler and its affiliated log file.
file_handler = logging.FileHandler('logfile.log')
# Keep only ERROR logs in the log file
file_handler.setLevel(logging.ERROR)
# Binding formatter to file handler
file_handler.setFormatter(formatter)
# Binding file handler to logger
logger.addHandler(file_handler)

##Use the defined logger below instead of logging module

logger.info("log message here")
#logger.exception("log message here")
```

17) If we want to have a traceback in errors in order to have more infos, use `logger.exception("log message here")` instead of `logger.error("log message here")`

18) If we want to see loggings on console in the phase of runnning, use stream handler. One logger can have 2 handlers, one of them is file handler and the other one might be stream handler.

```handlers.py
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# To show on console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Link handlers to loggers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Log messages
logger.info("log message here")

```

19) One of them most used formats is "{asctime} {levelname:<8} {message}" with style = "{"

```common_format.py
import logging
logging.basicConfig(format = "{asctime} {levelname:<8} {message}",  style = '{' )
```

20) Filemode can be either 'a' or 'w'. 'w' overrides the existing one.

21) If you are using try and except words in Python code, python logging is great to capture what is going on. It gives tracebacks etc.

```
a = 2

b = 0


try:
    mysub = a /b
except Exception as e:
    logging.critical("exception occurred: ",exc_info=True)
    #The above line prints traceback errors

```

21) The standard logging format is `'%(asctime)s - %(levelname)s - %(message)s'`.

22) filemode in logging.basicConfig() is either 'a' (append) or 'w' (write). 'w' deletes the log file and recreates it. 'a' just adds new logs to existing files.

23) We can add process id to logging.basicConfig via '%(process)d' to format attribute.

24) If we want to trace back the error, use one of the lines below based on your desired log level.

```error_traceback.py
logging.info("info level: ",exc_info=True)
logging.warning("warning level: ",exc_info=True)
logging.error("error level",exc_info=True)
logging.critical("warning level: ",exc_info=True)
```

25) We can define a configuration file in conf format or yaml format and load it in Python code like below.

```load_config_to_loggging.py
import logging
import logging.config
logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

```

26) We can set filemode either 'a'  (append) or 'w' (write) in logging.FileHandler(mode = 'w').

27) `The difference between different logging options are below:

- logger.error("message here"): will print out only error
- logger.error("message here", stack_info=True, exc_info=True): will print error, traceback and stack.
- logger.error("message here", exc_info=True): will print out error and traceback(same as **logger.exception("message here")**)
- logger.exception(e): will print out error and traceback (same as **logger.error("message here", exc_info=True)** )


28) [graypy](https://github.com/severb/graypy) is a python library to send python logs into Graylog in the format of GELF (Graylog Extended Log Format).

# Python Testing

1) Exploratory testing is a test without a plan.

2) In order to have a complete set of manual tests, what is required is to list all features our application has, different types of input it can accept and the expected results.

3) Testing multiple parts of our application is called **Integration testing**.

4) If you have many test files, create a folder named **tests** and locate your tests there.

5) Testing in Django and Flask is slightly different than unittest.

6) Functional tests follow 3A's principle.

- Arrange: the conditions for the test
- Act: calling some function or method
- Assert: check the condition is True

# Unit Testing

[Video Link](https://www.youtube.com/watch?v=6tNS--WetLI)

1) Good Unit Test will make sure that everything is working as it should.

2) Testing code with print statements isn't easy to automate. It is hard to maintain.

3) Naming convention: If we want to test a module named **calc.py**, testing file should be **test_calc.py**.

4) The methods in Class in testing file should start with **test_**. This is a naming convention. If we want to test add function, method name should be **test_add**.

5) We can obtain unittest assert methods from [here](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug).

6) To test the code, run the folloing on Terminal

```run.sh
python -m unittest test_calc.py
```

7) If we want to run in a way of `python test_calc.py` instead of `python -m unittest test_calc.py` , add the following to the bottom line of **test_calc.py**

```unittest_main.py
if __name__ == '__main__':
    unittest.main()
```

8) We should test a couple of edge cases(different scenarios for different inputs) instead of testing one scenario.

9) When we added 3 different `self.assertEqual(result,15)` to test_add method of TestCalc class, we run one test by 3 different checks.

10) If there are 4 tests in our test script and the third one failed, the output is like **. . F .**

11) assertRaises is taking 3 or more parameters like `self.assertRaises(ValueError,calc.divide,10,0)`. The **ValueError** is the error we want to see. **calc.divide** is the method we called. 10 and 0 are parameters we passed into **calc.divide**.  We aren't directly calling via calc.divide(10,0) because it raises a ValueError doesn't check the situation. However, testing exceptions aren't preferred mostly.

12) Testing exceptions via context managers are more preferrable like below

```
with self.assertRaises(ValueError):
    calc.divide(10,0)
```

13) Programmers try to make their code DRY(Don't repeat yourself). If we are using some piece of code in multiple tests, we should use `setUp()` and `tearDown()` method in out test. **setUp** method will run its code before every single test and **tearDown** method will run its code after every test. For instance, we can create a DB in `setUp()` and destroy it in `tearDown()`.

```file.py

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Muhammed','Buyukkinaci',5000)
        self.emp_2 = Employee('Ahmet','Yilmaz',4000)

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')


```

14) If we want to run a piece of code at the BEGINNING of tests just ONCE, we can use **setUpClass(cls)** method. If we want to run a piece of code at the END of tests just ONCE, we can use **tearDownClass(cls)**. They are classmethods and no need to create an instance from the class. An example usage is to read a table from DB and use it in all test scenarios.

```file.py
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
    
        print('tearDownClass')

    def test_something1(self):
        print("test_something1")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')

    def test_something2(self):
        print("test_something2")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')
    
    def test_something3(self):
        print("test_something3")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')

    # The output is as follows:

    # setUpClass
    # test_something1
    # test_something2
    # test_something3
    # tearDownClass

```

15) In short, mocking is creating objects that simulate the behavior of real objects in unit testing. The aim of mocking is to isolate and focus on the code, not to focus on extermal resources. Mocking means creating a fake version of an external or internal service that can stand in for the real one.

16) For example, we wrote a function which scrapes data from a website. However, the website was down. Therefore, our tests would fail. This isn't what we want. In this scenario, using mocks in unit testing sound logical.

17) Test should be isolated. Your tests shouldn't rely on other tests or affet other tests. Run each test independently.

18) Test Driven Development is that you write tests before you write the code.

19) Any testing is better than no testing. Even if you write some basic assertions, It is better than nothing.

20) unittest module in Python is originally inspired from Java's JUnit.

# Pytest

[Video Link 1](https://www.youtube.com/watch?v=etosV2IWBF0)

[Video Link 2](https://www.youtube.com/watch?v=fv259R38gqc)

[Blog Post](https://realpython.com/pytest-python-testing/)

1) Test is code that runs to check the validity of other code.

2) Pytest is the basis for a rich ecosystem of testing plugins and extensions.

3) `assert` is the way to do testing in Pytest

4) Ist API is easier than unittest API.

![property](./images/002.png)

5) pytest looks for a file starting with test_. Also, the name of function to be tested should start with test_

6) If there are 2 assertions in one function, it is one test; not 2 tests.

7) The test should be roughly divided into 3 phases: **Arrange**, **Act**, **Assert**. Arrange is setting up anything that needs to go before the action happens.

8) In test driven development, declare something that clearly doesn't exist yet. We want test to drive out what it is I want to make.

9) Functions names in test file must be unique.

10) The reason why we write tests is to validate our code and not to have to go through process of manually checking things over and over again.

11) Assert by themselves without pytest can explode our code if assert is False

12) Using try/except in Python means "I give up, I don't know how to do this. Somebody above me, please handle this".

13) If we want to raise an error and run our test properly, use below

```demo.py
def add(a,b):
    if a==99:
        raise MysteryError()
    return a + b
```

```test_demo.py
def test_error():
    # Waiting the code to fail. The test runs properly in terminal
    with pytest.raises(demo.MysteryError):
        demo.add(99,1)s
```

14) If the first assertion in test method fails, it aborts the rest of the test.

```test_demo.py
def test_sth():
    assert 1 == 1 # running and successful
    assert 2 == 1 # running and fail; the below asserts not run
    assert 3 > 2 # not running
```

15) Pytest has a feature called parametrize to run all asserts even if the above asset fails to run. If we have multiple failures in test, we have multiple error log chunks. It is a useful tool if you want to test your code against a bunch of
scenarios.

16) We can group tests in test files via creating Classes like TestAdd.

17) Fixtures have various capabilities. Each test using fixture must explicitly accept that fixture as an argument.
- Fixtures allow us to set up some import things before each test to runlike unittest's setUp and tearDown methods.Fixtures are for setup/reuse purposes. 
- Fixtures are providing data.
- Fixtures are also similar to unittest's mocking.

18) Create a conftext.py and define a fixture named *my_fixture*. Feed this **my_fixture** in test_fixture of test_demo.py.

```conftest.py
import pytest
@pytest.fixture
def my_fixture():
    return 51
```

```test_demo.py
def test_fixture(my_fixture):
    assert my_fixture ==51
```

19) There is a library called pytest django, which is an extension to Django Framework.

20) capsys is a pretty cool tool to capture system output.

21) Mnkeypatch is a fixture. monkeypatching is a terminology used when you want to dynamically add runtimes, swap out the behavior of a thing.

22) tmpdir is creating a new file and prints results on it and delete it ultimately.

23) Multiple fixtures operate at the same time.

24) Pytest's fixture mechanism is implicit and hard to understand here this idea comes from.

25) To list available fixtures on Terminal

```
pytest --fixtures
```

26) F means test failed and E means there is an unexpected exception.

27) If we have 4 tests in our script and only want to test 2 of these 4, filter them via pytest -k 'test_add'. Usage is `pytest test_demo.py -k 'test_with_param'`.

```test_filter_based_on_name.py
def test_add_tuple():
    #some code here
def test_add_list():
    #some code here
def test_subtract_tuple():
    #some code here
def test_subtract_tuple():
    #some code here
```

28) We can assign marks to our tests and check only these tests via -m parameter on console. A test may have multiple marks. Example: `pytest test_demo.py -k 'test_with_param'`

29) If we write 2 tests and both are using the same data, we can define a fixture via `@pytest.fixture` decorator and pass the fixture via argument into test method.

30) We should move fixtures to a different module(conftest.py) and import fixtures from test script.

31) After assigning marks to tests, register them on *pytest.ini*.

```pytest.ini
# content of pytest.ini. pytest.ini located in where pytest is executed.
[pytest]
markers =
    basics: basic assertions
    addition: a marker meaning addition
```

32) To run test in test_demo.py whose marks are 'basics'

```
pytest test_demo.py -m basics
```

33) Default markers are below obtained via `pytest --markers`:

- @pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.- html#pytest-mark-filterwarnings 

- @pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") - skips the test.

- @pytest.mark.skipif(condition, ..., *, reason=...): skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.- platform == 'win32') skips the test if we are on the win32 platform. See https://docs.pytest.org/en/stable/reference/reference.- html#pytest-mark-skipif

- @pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict): mark the test function as an expected failure if - any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test - function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a - true failure. See https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail

- @pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally - needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: - @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.- pytest.org/en/stable/how-to/parametrize.html for more info and examples.

- @pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/- stable/explanation/fixtures.html#usefixtures 

- @pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.

- @pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.

34) To show the slowest 3 tests

```
pytest --durations=3
```

35) Some useful Pytest plugins:

- pytest-randomly
- pytest-cov
- pytest-django
- pytest-bdd

# Unit Testing for Data Science

[Video Link](https://www.youtube.com/watch?v=Da-FL_1i6ps)

1) Different types of tests

![property](./images/003.png)

2) Unit testing is all about isolation.

3) Writing test as early as thy can be valuable.

4) Some useful options for pytest

![property](./images/004.png)

5) pandas's testing module is useful in testing. To check 2 dataframe are equal:

```pandas_unittesting.py
# Writes the below code in test function or test method
pd.testing.assert_frame_equal(actual,expected)

from pandas.util.testing import assert_frame_equal(df1,df2,
    check_like=True, # order doesn't matter
    check_dtype = False, # check for identical data types
    check_less_precise = 4 # number of digits to compare
)
from pandas.util.testing import assert_index_equal
from pandas.util.testing import assert_series_equal


```

6) Fixtures are a modular approach to setup & teardown methods. Fixtures are generally defined in conftest.py and imported in test_sth.py and passed as arguments to methods or functions.

7) An example usage of fixtures in pytest

![property](./images/005.png)

8) To list all possible default fixtures, run `pytest --fixtures`.

9) We can define scopes to fixtures by passing argument to them. session is a parameter passed to fixture and meaning that it is run once in a session of testing

```conftest.py

@pytest.fixture(scope='session')
def spark(request):

    spark = (SparkSession
    .builder
    .appName('Pytest-example')
    .master('local[2]')
    .getOrCreate()
    )

    request.addfinalizer(lambda : spark.stop())

    return spark

#spark fixtures passed to spark_df fixture
@pytest.fixture()
def spark_df(spark):
    return spark.createDataFrame(
        [('a','b'),
        ('a','b')
        ],
        ['col_a','col_b']
    )

```

10) We can use a fixture in another fixture in conftest.py like above.

11) Mocking in pytest

![property](./images/006.png)

12) Where to use mocks 

- Database reads and writes

- API calls

- External functions we don't want to test 

13) Example usage of mocks

![property](./images/007.png)

14) Mock objects where they are used, not where they are defined

```
# The correct one:
@mock.patch('pytest_examples.functions_to_test.pd.read_csv')
# The incorrect one
@mock.patch('pandas.read_csv')

```

15) Don't forget to pay attention to decorator order

![property](./images/008.png)

16) Not to forget to use assertions on your code. Aserrtions are our best

```
a = 2

# assert expression, 'Exception you defined'
assert 1 > a, 'the input bigger than 1'
```

17) For one-off analyses, writing tests isn't advised. Focusing on clear documentation sounds more logical.
 




