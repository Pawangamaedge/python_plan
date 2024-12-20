# sequence of character that form the search pattern in the string
# used to check if a string contains any specified search pattern

import re

# search function
s='python is high level programming laguage which has many modules'
word=re.search('has',s)  # returns the search object if there is any match in string 
print(word)
print(f"starting index: {word.start()}") # starting index of the string
print(f"ending index: {word.end()}")  # ending index of the string

# find all function
st="this is high level 91 number which has 2 digits and next number will be 99"
num=re.findall('\d+',st) # returns the list contains matching
num2=re.findall('\d',st) 
print(num)
print(num2)

# compile funcion
comp=re.compile('[a-e]')  # performing the string substitutions and returns the list 
print(comp.findall("this is abs value directly coming"))

rgx=re.compile('\w') # finds the list of word character form the string 
print(rgx.findall("he said ( * ) some & language"))

rgx1=re.compile('\w+') # finds the sequence of word character
print(rgx1.findall("I went to him at 11 A.M., he \ said *** in some_language."))

rgx2=re.compile('\W') # finds the non word characters 
print(rgx2.findall("he \ said *&* in some_language"))

rgx3=re.compile('\w+') # finds the word characters 
print(rgx3.findall("he \ said *&* in some_language"))

print(re.findall('[a-s]',st))
print(re.findall('le..l',st))
print(re.findall('language|level',st))