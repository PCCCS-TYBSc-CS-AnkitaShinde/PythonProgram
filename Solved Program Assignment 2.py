#Accessing String Elements
msg = 'Hello'
a = msg[0]
print(a)
b = msg[4]
print(b)
c = msg[-0]
print(c)
d = msg[-1]
print(d)
e = msg[-2]
print(e)
f = msg[-5]
print(f)
msg = 'Rafting'
print(msg[3:100])

#String Properties
msg = 'Surreal'
print(type(msg))
print(id(msg))

msg = 'Hello'
print(msg.replace('l','L'))
print("-".join("Hello"))
print(msg.upper())
print('Hello'.upper())

age = 25
print('She is' + str(age) + 'years old')
i = int("34")
f = float("3.14")
c = complex("3+2j")
print(ord('A'))
print(chr(65))


# String Comparison
s1 = "Bombay"
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"
print(s1 == s2)
print(s1 == s5)
print(s1 != s3)
print(s1 > s4)
print(s1 < s2)
print(s1 <= s4)

#Programs
#1
''' Demonstrate hoe to create simple and multi-line strings and whether a string
can change after creation. Also show the usage of built-in functions len(),min
and max() on a string'''

# Simple strings
msg1 = 'Hoopla'
print(msg1)

#Strings with special characters
msg2 = 'He said,\'Let Us Python\'.'
file1 = 'C:\\temp\\newfile'
file2 = r'C:\\temp\\newfile'
print(msg2)
print(file1)
print(file2)

#multiline strings
# whitespace at beginning of second line becomes part of string
msg3 = 'What is this life if full of care...\
        We have no time to stand and stare'

#enter at the end of first line becomes par of string
msg4 = """What is this life if full of care...
We have no time to stand and stare"""

# strings are concatenated properly.()necessary
msg5 = ('What is this life if full of care...'
        'We have no time to stand and stare')
print(msg3)
print(msg4)
print(msg5)

#string replication during printing
msg6 = 'MacLearn!!'
print(msg1 * 3)

#immutability of strings
#Utopia cannot change, msg7 can
msg7 = 'Utopia'
msg8 = 'Today!!!'
msg7 = msg7 + msg8
print(msg7)
# use of built-in functons on strings
print(len('Hoopla'))
print(min('Hoopla'))
print(max(('Hoopla')))

#2
# For a given string 'Bambloozed', write a program to obtain the following output:

s = 'Bamboozled'
#extract B a
print(s[0],s[1])
print(s[-10],s[-9])
#extract e d
print(s[8],s[9])
print(s[-2],s[-1])
#extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8:])
#extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])
print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])
S = s+'Hype!'
print(S)
S = s[:6]+'Monger!'
print(S)

#3
'''For the following strings find out which are having only alphabets, which are numeric, which are
alphanumeric, which are lowercase, which are uppercase. Also find out whether 'And Quiet Flows The Don'
begins with 'And' or ends with 'And' :
'NitiAayog'
'And Quiet Flows The Don'
'1234567890'
'Make $1000 a day' '''

s1 = 'NitiAayog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)
print('s4 =', s4)
# Content test functions
print('check isaplpha on s1, s2')
print(s1.isalpha())
print(s2.isalpha())
print('check isdigit on s3, s4')
print(s3.isdigit())
print(s4.isdigit())
print('check isalnum on s1. s2, s3, s4')
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())
print('check islower on s1, s2')
print(s1.islower())
print(s2.islower())
print('check isupper on s1, s2')
print(s1.isupper())
print(s2.isupper())
print('check startswith and endswith on s2')
print(s2.startswith('And'))
print(s2.endswith('And'))

#4
'''Given the following string:
'Bring it on'
' Flanked by spaces on either side'
'C:\\Users\\Kanetkar\\Documents'
write a program to produce the following output '''

s1 = 'Bring It On'
# Conversions
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
#search and replace
print(s1.find('I'))
print(s1.find('On'))
print(s1.replace('It', 'Him'))
#trimming
s2 = ' Flankedcby spaces on either side '
print(s2.lstrip())
print(s2.rstrip())
#splitting
s3 = 'C:\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print((s3).partition('\\'))

#5
'''Find all occurences of 'T' in the string 'The Terrible Tiger Tore The Towel'
Replace all occurences of 'T' with 't' '''

s ='The Terrible Tiger Tore The Towerl'
pos = s.find('T',0)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos,s[pos])
pos = s.find('T',pos + 1)
print(pos)
c = s.count('T')
s = s.replace('T','t',c)
print(s)

