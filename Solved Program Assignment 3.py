# Naunces of conditions
print(bool(3.14))
print(bool(25))
print(bool(0))
# Logical operators
a = 40
b = 30
x = 75 and a >= 20 and b < 60 and 35
y = -30 and a >= 20 and b < 15 and 35
z = -30 and a >= 20 and 0 and 35
print(x)
print(y)
print(z)
x = 75 or a >= 20 or b < 60
y = a >= 20 or 75 or 60
z = a < 20 or 0 or 35
print(x)
print(y)
print(z)
a = 10
b = 20
print(not(a <= b))
print(not(a >= b))

# Conditional Expression
age = 15
status = 'minor' if age < 18 else 'adult'
sunny = False
print('Lets go to the','beach' if sunny else 'room' )
humidity = 76.8
setting = 25 if humidity > 75 else 28
print(setting)

# assign Prim
wt = 55
msg = 'Obese' if wt > 85 else 'Hefty'  if wt > 60 else 'Prim'
print(msg)

# all() and any()
a,b,c = 10,20,30
res = all((a>5, b>20, c,15))
print(res)
res = any((a>5, b>20, c>15))
print(res)

# Receiving input
name =input('Enter your name: ')
age = int(input('Enter your age: '))
salary = float(input('Enter your salary:'))
print(name,age,salary)

#Programs
# 1
'''While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than
1000. If quantity and price per item are input through the keyboard, write a program to calculate the
 total expenses'''

qty = int(input('Enter value of quantity'))
price = float(input('Enter value of price'))
if qty > 1000:
    dis = 10
else:
    dis = 0
totexp = qty * price - qty * price * dis / 100
print(('Total expenses = Rs.' + str(totexp)))

# 2
''' In a company an employee is as under:
If the basic salary is less than Rs.1500, then HRA = 10% of basic salary and DA=90% of basic salary.
If his salary is either equal to or above Rs.1500, then HRA = Rs.500 and DA = 98% of basic salary.
If the employees salary is input through the leyboard write a program to find his gross salary.'''

bs = int(input('Enter value of bs:'))
if bs > 1000:
    hra = bs * 15/100
    da = bs * 95/100
    ca = bs * 10/100
else:
    hra = bs * 10 / 100
    da = bs * 90/ 100
    ca = bs * 5 / 100
gs = bs + da + hra + ca
print('Gross Salary= Rs.'+str(gs))

# 3
'''Percentage marks obtained by a student are input through the keyboard the keyboard.
The student gets a division as per the following rules:
Percentage above or equal to 60 - First division
Percentage between 50 and 59 - Second division
Percentage between 40 and 49 - Third division
Percentage less than 40 - Fail
Write a program to calculate the division obtained by the student.'''

per = int(input('Enter value of percentage:'))
if per >= 60:
    print('First Division')
elif per >= 50:
    print('Second Division')
elif per >= 40:
    print('Third Division')
else:
    print('Fail')

# 4
'''A company insures its drivers in the following cases:
- If the driver is married.
- If the driver is unmarried, male & above 30 years of age.
- If the driver is unmarried, female & above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex and age of
the driver are the inputs, write a program to determine whether the driver should
 be insured or not.'''

ms = input('Enter marital status:')
s = input('Enter sex:')
age = int(input('Enter age:'))
if (ms == 'm') or (ms == 'u' and s == 'm' and age > 30) \
        or (ms == 'u' and s == 'f' and age > 25):
    print('Insured')
else:
    print('Not Insured')

# 5
'''Suppose there are four flag variables w, x, y, z. Write a program to check in
multiple ways whether ine of them is true.'''

# Different ways to test multiple flags
w,x,y,z = 0,1,0,1
if w == 1 or x == 1 or y == 1 or z == 1:
    print('True')
if w or x or y or z:
    print('True')
if any((w,x,y,z)):
    print('True')
    if 1 in (w,x,y,z):
        print('True')



