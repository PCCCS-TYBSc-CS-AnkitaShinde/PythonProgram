# What will be the output of the following programs:
#a]
i,j,k = 4,-1,0
w = i or j or k
x = i and j and k
y = i or j and k
z = i and j or k
print(w,x,y,z)

#b]
a = 10
a = not not a
print(a)

#c]
x,y,z = 20,40,45
if x > y and x > z:
    print('biggest=' + str(x))
elif y > x and y > z:
    print('biggest = ' + str(y))
elif z > x and z > y:
    print('biggest = ' + str(z))

#d
num = 30
k = 100 if num <= 10 else 500
print(k)



#e]
a = 10
b = 60
if a and b > 20:
    print('Hello')
else:
    print('Hi')

#f]
a = 10
b = 60
if a > 20 and b > 20:
    print('Hello')
else:
    print('Hi')

'''g]
a = 10
ifa = 30 or 40 or 60:
    print('Hello')
else:
    print('Hi')                 #outout = error '''
# What will be the output of the following programs:

'''h]
a = 10
if a = 30 or a == 40 or a == 60 :
     print('Hello')
else:
     print('Hi')        # output= error '''

# i]
a = 10
if a in (30,40,50):
    print('Hello')
else:
    print('Hi')
# If a = 10, b = 12, c = 0, find the values of the following expressions
a = 10
b = 12
c = 0
x = a!=6 and b > 5
y = a == 9 or b < 3
z = not(a < 10)
u = not(a > 5 and c)
v = 5 and c!=8 or c
print(x)
print(y)
print(z)
print(u)
print(v)


''' Any integer is input thruough the keyboard. Write a program to find out whether
 it is an odd number or even number'''


# Determine whether number is odd or even
x = int(input('Enter any number:'))
j = 2
if x % j == 0:
    print('Even Number')
else:
    print('Odd Number')





'''Any year is input through the keyboard. Write a program to dermine whether the year
is a leap year or not.'''

# Determine whether year is leap or not
year = int(input('Enter a year:'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,'is a Leap Year')
        else:
            print(year,'is not a Leap Year')
    else:
        print(year,'is a Leap Year')
else:
    print(year,'is not a Leap Year')


''' If ages of Ram, Shyam and Ajay are input through the keyboard, write a program to
determine the youngest of the three.'''

ram_age = int(input('Enter Ram\'.s age:'))
shyam_age = int(input('Enter Shyam\'.s age:'))
ajay_age = int(input('Enter Ajay\'.s age:'))
if ram_age < shyam_age and ram_age < ajay_age:
    print('Youngest is Ram')
elif shyam_age < ram_age and shyam_age < ajay_age:
    print('Youngest is Shyam')
elif ajay_age < ram_age and ajay_age < shyam_age:
    print('Youngest is Ajay')

'''Write a program to check whether a triangle is valid or not, when the three angles
of the triangle are entered through the keyboard. A trianle is valid if the sum of all
the three angles is equal to 180 degrees'''

# Determine whether triangle is valid or not
x = int(input('Enter angle no.1 :'))
y = int(input('Enter angle no.2:'))
z = int(input('Enter angle no.3:'))
sum_of_angles = x + y + z
if sum_of_angles == 180:
    print('Valid Triangle')
else:
    print('Inalid Triangle')


# Write a program to find the absolute value of a number entered through the keyboard.

# Obtain absolute value of a number
x = int(input('Enter any number:'))
if x < 0:
    y = x*(-1)
else:
    y = x
print('Absolute value of',x,'is',y)

'''Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater then its perimeter. For example, the area of the rectangle with length = 5
and breadth = 4 is greater than its perimeter'''

#Determine whether area of rectangle is grater than its perimeter
length = int(input('Enter the length of rectangle:'))
breadth = int(input('Enter the breadth of rectangle:'))
area = length * breadth
perimeter = 2 * (length + breadth)
print('Area=',area,'Perimeter=',perimeter)
if area > perimeter:
    print('Area of Rectangle is grater than perimeter')
else:
    print('Perimeter of rectangle is greater than area')

'''Given three points(x1,y1),(x2,y2) and (x3,y3), write a program to check if all the
three points fall on one straight line.'''

# Determine whether 3 points are collinear
x1 = int(input('Enter the co-ordinates of x1:'))
y1 = int(input('Enter the co-ordinates of y1:'))
x2 = int(input('Enter the co-ordinates of x2:'))
y2 = int(input('Enter the co-ordinates of y2:'))
x3 = int(input('Enter the co-ordinates of x3:'))
y3 = int(input('Enter the co-ordinates of y3:'))
if x1 == x2 and x2 == x3:
    print('Collinear')
elif x1 != x2 and x2 != x3 and x3 != x1:
    # Calculate Slope of line between each pair of points
    s1 = (float(abs(y2 - y1))) / (float(abs(x2 - x1)))
    s2 = (float(abs(y3 - y2))) / (float(abs(x3 - x2)))
    s3 = (float(abs(y3 - y1))) / (float(abs(x3 - x1)))
if s1 == s2 and s2 == s3:
    print('Three points are Collinear')
else:
    print('Three point are Non Collinear')




'''Given the coordinates(x,y) of center of a circle and its radius, write a program that
will determine whether a point lies inside the circle, on the circle or outside the circle'''

# Determine whether point lies inside, outside or on the circle
import math
centerX = int(input('Enter X coord. of center of circle:'))
centerY = int(input('Enter Y coord. of center of circle:'))
radius = int(input('Enter radius of circle:'))
print('Enter coordinates of point:')
pointX = int(input('Enter the X coord. of point'))
pointY = int(input('Enter the Y coord. of point'))
xDiff = centerX - pointX;
yDiff = centerY - pointY;
distance = math.sqrt((xDiff * xDiff) + (yDiff * yDiff))

if distance == radius:
    print('Point is on the circle')
elif distance < radius:
    print('Point lies inside the circle')
else:
    print('Point lies outside the circle')






'''Given a point (x,y), write a program to find out if it lies on the
X-axis, Y=axis or on the orign '''

#Determine where a point lies in coordinate system
x = int(input('Enter X Coord of the point:'))
y = int(input('Enter Y Coord of the point:'))
if x == 0 and y == 0:
    print('Point is the origin')
elif x == 0 and y != 0:
    print('Point lies on the Y axis')
elif x != 0 and y == 0:
    print('Point lies on the X axis')
else:
    if x > 0 and y > 0:
        print('Point lies in the First Quadrant')
    elif x < 0 and y > 0:
        print('Point lies in the Second Quadrant')
    elif x < 0 and y < 0:
        print('Point lies in the Third Quadrant')
    else:
        print('Point lies in the Fourth Quadrant')




'''A year is entered through the keyboard, write a program to determine whether the year
is leap or not. Use the logical opertors and and or '''

# Determine whether year is leap or not
year = int(input('Enter a year:'))
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')


'''If the three sides of a triangle are entered through the keyboard, write a program to
check whether the triangle is valid or not. the triangle is valid if the sum of two sides
is greater than the largest of the three sides'''

#Determine whether triangle is valid or not
s1 = int(input('Enter the 1st side of triangle:'))
s2 = int(input('Enter the 2nd side of triangle:'))
s3 = int(input('Enter the 3rd side of triangle:'))
if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:
    print('Invalid Triangle')
else:
    print('Valid Triangle')

'''If the three sides of a triangle are entered through the keyboard, write a program
to check whether the triangle is isosceles, equilateral, scalene or right angled triangle.'''

# Determine the type of triangle
s1 = int(input('Enter the 1st side of triangle:'))
s2 = int(input('Enter the 2nd side of triangle:'))
s3 = int(input('Enter the 3rd side of triangle:'))
if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:
    print('The side do not form a triangle')
else:
    if s1 != s2 and s2 != s3 and s3 != s1:
        print('Scalene Triangle')
    if s1 == s2 and s2 != s3:
        print('Isosceles triangle')
    if s2 == s3 and s3 != s1:
        print('Isosceles triangle')
    if s1 == s3 and s3 != s2:
        print('Isosceles triangle')
    if s1 == s2 and s2 == s3:
        print('Equilateral triangle')
a = (s1 * s1) == (s2 * s2) + (s3 * s3)
b = (s2 * s2) == (s1 * s1) + (s3 * s3)
c = (s3 * s3) == (s1 * s1) + (s2 * s2)
if a or b or c:
    print('Right-angled triangle')



