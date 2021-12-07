# Variable type and Assignment
print(type(35))
print(type(3.14))
a = 10
print(type(a))
a = 31.4
print(type(a))
a = 'Hi'
print(type(a))
a = 'Jamboree'
print(type(a))
a = 10
print(a)
pi = 3.14
print(pi)
name = 'Sanjay'
print(name)

# Arithmetic Opertors
a = 4/2
print(a)
a = 7 % 2
print(a)
b = 3 ** 4
print(b)
c = 4 // 3
print(b)
a **= 3
print(a)
b %= 10
print(b)

# Operation Naunce
print(10//3)
print(-10//3)
print(10//-3)
print(-10//-3)
print(3//10)
print(3//-10)
print(-3//10)
print(-3//-10)
print(10 % 3)
print(-10 % 3)
print(10 % -3)
print(-10 % -3)
print(3 % 10)
print(3 % -10)
print(-3 % 10)
print(-3 % -10)

# Built-in functions
a = abs(-3)
print(a)
print(min(10, 20, 30, 40))
print(hex(26))

# Built-in modules
import math
import random
print(math.factorial(5))
print(math.degrees(math.pi))
print(random.random())
# Container types
lst = [10, 20, 30, 20, 30, 40, 50, 10]
tpl = ('Let Us Python', 350, 195.00)
s = {10, 20, 30, 40}
dct = {'ME101': 'SOM', 'EE101': 'Electronics'}
print(lst[0], tpl[2])
print(dct['ME101'])

# Classes and Objects
a = 30
b = 'Good'
print(a, b)
print(type(a), type(b))
print(id(a), id(b))
print(isinstance(a, int), isinstance(b, str))

# Multiple Objects
a = 3
b = 3
print(id(a), id(b))
print(a is b)
a = 30
print(id(a))

# programs
# 1.
#Demonstrate use of integer types and operators that can be used on them.

# use of integer types
print(3 / 4)
print(3 % 4)
print(3 // 4)
print(3 ** 4)
a = 10; b = 25; c = 15; d = 30; e = 2; f = 3; g = 5
w = a + b - c
x = d ** e
y = f % g
print(w, x, y)
h = 99999999999999999
i = 54321
print(h * i)

# 2.
#Demonstrate use of float, complex and bool types and operators that can be used on them

# use of float
i = 3.5
j = 1.2
print(i % j)

# use of complex
a = 1+2j
b = 3 * (1 + 2j)
c = a * b
print(a)
print(b)
print(c)
print(a.real)
print(a.imag)
print(a.conjugate())
print(a)

# use of bool
x = True
y = 3 > 4
print(x)
print(y)


# 3.
# Demonstrate how to convert from one number type to another.
# convert to int
print(int(3.14))
a = int('485')
b = int('768')
c = a + b
print(c)
print(int('1011', 2))
print(int('341', 8))
print(int('21', 16))

# convert to float
print(float(35))
i = float('4.85')
j = float('7.68')
k = i + j
print(k)

# convert to complex
print(complex(35))
x = complex(4.85, 1.1)
y = complex(7.68, 2.1)
z = x + y
print(z)

# convert to bool
print(bool(35))
print(bool(1.2))
print(int(True))
print(int(False))

# 4.
# Write a program that makes use of built-in mathematical functions.

# built-in functions
print(abs(-25))
print(pow(2, 4))
print(min(10, 20, 30, 40, 50))
print(max(10, 20, 30, 40, 50))
print(divmod(17, 3))
print(bin(64), oct(64), hex(64))
print(round(2.567), round(2.5678, 2))

# 5.
# Write a program that makes use of functions in the math module.

# mathematical functions from math module
import math
x = 1.5357
print(math.pi, math.e)
print(math.sqrt(x))
print(math.factorial(6))
print(math.fabs(x))
print(math.log(x))
print(math.log10(x))
print(math.exp(x))
print(math.trunc(x))
print(math.floor(x))
print(math.ceil(x))
print(math.trunc(-x))
print(math.floor(-x))
print(math.ceil(-x))
print(math.modf(x))


# 6.
#Write a program that generates float and integer random numbers.

# random number operations using random module
import random
import datetime
random.seed(datetime.time())
print(random.random())
print(random.random())
print(random.randint(10, 100))

# 7.
'''HOw will you identify which of the following is a string, list, tuple, set or directory?
{10,20,30.5}
{12:'Simple},43:'Complicated',13:'Complex'}
"Check it out!"
3+2j'''

# determine type of dataA
print(type({10, 20, 30.5}))
print(type([1, 2, 3.14, 'Nagpur']))
print(type({12: 'Simple', 43: 'Complicated', 13: 'Complex'}))
print(type("Check it out!"))
print(type(3 + 2j))
