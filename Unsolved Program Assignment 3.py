#a
''' Write a program that swaps the values of variables a and b. You are not
allowed to use a third variable. You are not allowed to perform arithmetic on a and b.'''

a = input('Enter value of a: ')
b = input('Enter value of b: ')
a,b = b,a
print("After Swapping ")
print("Value of a:",a)
print("Value of b:",b)
#b
# Write a program that makes use of trigonometric functions available in math  module.

import math
a = 1
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))
print(math.sinh(a))
print(math.cosh(a))
print(math.tanh(a))
print(math.asin(a))
print(math.acos(a))
print(math.atan(a))
#c
'''Write a program that generates 5 random numbers in the range 10 to 50.
 Use a seed value of 6. Make a provision to change this seed value
  every time you execute the program by associating it with time of execution?'''
import random
import time

random.seed(6)
for i in range(5):
    print(random.randint(10,50))

print()
t = int(time.time())
random.seed(t)

for i in range(5):
    print(random.randint(10,50))
#d
#	Write a program that makes use of trigonometric functions available in math  module.

'''Use trunc(), floor() and ceil() for numbers -2.8, -0.5, 0.2, 1.5 and 2.9
to understand the difference between these functions clearly.'''

import math
a = -2.8
b = -0.5
c = 0.2
d = 1.5
e = 2.9
print(math.trunc(a))
print(math.floor(a))
print(math.ceil(a))
print(math.trunc(b))
print(math.floor(b))
print(math.ceil(b))
print(math.trunc(c))
print(math.floor(c))
print(math.ceil(c))
print(math.trunc(d))
print(math.floor(d))
print(math.ceil(d))
print(math.trunc(e))
print(math.floor(e))
print(math.ceil(e))

#e
'''Assume a suitable value for temperature of a city in Fahrenheit degrees. Write a 
program to convert this temperature into Centigrade degrees and print both temperatures'''


fahrenheit = float(input("Enter temperature in fahrenheit: "))
centrigate  = (fahrenheit - 32) * 5/9
print('%0.2f Fahrenheit is:%0.2f Celsius' %(fahrenheit, centrigate))
#f
'''Given three sides a, b, c of a triangle,
write a program to obtain and print values of three angles rounded to the next integer.
 Use the formulae: a2=b2+c2-2bc cos A, b2= a2+c2- 2ac cos B,c2 = a2 + b2 – 2ab cos C '''

import math
a,b,c = [int(a) for a in input("Enter three sides of triangle: ").split()]
alpha = math.acos((b*b + c*c- a*a) /(2 * b * c));
betta = math.acos((a*a + c*c - b*b) /(2 * a * c));
gamma = math.acos((a*a + b*b - c*c) /(2 * a * b));
alpha = alpha * 180 / math.pi;
betta = betta * 180 / math.pi;
gamma = gamma * 180 / math.pi;
print("alpha",alpha)
print("betta",betta)
print("gamma",gamma)

# a.	Print imaginary part out of 2 + 3j.
a = 2 + 3j
print(a.imag)
#b.	Obtain conjugate of 4 + 2j.
a = 4 + 2j
b = a.conjugate()
print(b)
# c. Print decimal equivalent of binary ‘1100001110’
print(int('1100001110',2))
#d.	Convert a float value 4.33 into a numeric string.
a = str(4.33)
print(a)
#e.	Obtain integer quotient and remainder while dividing 29 with 5.
x = divmod(29,5)
print(x)
#f.	Obtain hexadecimal equivalent of decimal 34567.
y = hex(34567)
print(y)
#g.	Round-off 45.6782 to second decimal place.
z = round(45.6782)
print(z)
#h.	Obtain 4 from 3.556.
a = round(3.556)
print(a)
#i.	Obtain 17 from 16.7844.
b = round(16.7844)
print(b)
#j.	Obtain remainder on dividing 3.45 with 1.22.
a = 3.45 % 1.22
print(a)






