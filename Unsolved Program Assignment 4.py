#a
'''Write a program that generates the following output from the string ‘Shenanigan’.
S h
a n
enanigan
Shenan
Shenan
Shenan
Shenan
Shenanigan
Seaia
Snin
Saa
ShenaniganType
ShenanWabbite'''
s = 'Shenanigan'

print(s[0],s[1])    #extract S h
print(s[4],s[5])    #extract a n
print(s[2:])        #extract enanigan
print(s[0:6])       #extract Shenan
print(s[:6])
print(s[-10:-4])
print(s[:-4])
print(s)            #extract Shenanigan
print(s[0:10:2])        #extract Seaia
print(s[0:10:3])        # extract Snin
print(s[0:10:4])        # extract Saa
print(s+'Type')         # extract ShenaniganType
print(s[:6]+'Wabbite')      # extract ShenanWabbite

#b
'''Write a program to convert the following string
‘Visit ykanetkar.com for online course in programming’
into
‘Visit Ykanetkar.com For Online Course In Programming' '''

s = 'Visit ykanetkar.com for online course in programming'
print(s.title())



#c
'''Write a program to convert the following string
‘Light travels faster than sound. This is why some people appear bright until you hear them speak.’
into
‘LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak.'''

s = 'Light travels faster than sound. This is why some people appear bright until you hear them speak.'
print(s.replace('Light','LIGHT').replace('sound','SOUND'))


#d
# What will be the output of the following program?

s= 'HumptyDumpty'
print('s = ',s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('Hump'))
print(s.endswith('Dump'))


#f
'''If we wish to work with an individual word in the followin
g string, how will you separate them out:
‘The difference between stupidity and genius is that genius has its limits’ '''

msg = "The difference between stupidity and genius is that genius has its limits"
for word in msg.split():
    print(word)



'''What will be the output of the following code snippet?
print(id(‘Imaginary’))
print(type(‘Imaginary’))'''

print(id("Imaginary"))
print(type("Imaginary"))

'''What will be the output of the following code snippet?
s3 = ‘C:\\Users\\Kanetkar\\Documents’
print(s3.split(‘\\’))
print(s3.partition(‘\\’))'''

s3 = "C:\\Users\\Kanetkar\\Documents"
print(s3.split("\\"))
print(s3.partition("\\"))

'''How will you eliminate spaces on either side of the string
‘ Flanked by spaces on either side ’?'''
name= " Flanked by spaces on either side "
print(name.strip())

'''What will be the output of the following code snippet?
s1 = s2 = s3 = “Hello”
Print(id(s1), id(s2), id(s3))'''
s1 = s2 = s3 = 'Hello'
print(id(s1), id(s2), id(s3))

'''What will  get sorted in ch in the following snippet:
msg = ‘Aeroplane’
ch = msg[-0]'''
msg = "Aeroplane"
ch = msg[-0]
print(ch)

