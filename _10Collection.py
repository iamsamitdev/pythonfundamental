Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Collections in Python with str,bytes,list,dict
>>> "inconsitant'
SyntaxError: EOL while scanning string literal
>>> "it's a good thing."
"it's a good thing."
>>> '"Yes!", he said, "I agree!"'
'"Yes!", he said, "I agree!"'
>>> 
print('"Yes!", he said, "I agree!"')
"Yes!", he said, "I agree!"
>>> "first" "second"
'firstsecond'
>>> """This is
a multiline
string"""
'This is\na multiline\nstring'
>>> "Hello\n\nMy name is Samit"
'Hello\n\nMy name is Samit'
>>> print("Hello\n\nMy name is Samit")
Hello

My name is Samit
>>> print('I\'m a teacher')
I'm a teacher
>>> k = 'A \\ in a string.'
>>> k
'A \\ in a string.'
>>> print(k)
A \ in a string.
>>> path = r'C:\Users\Samit\Documents\Spells'
>>> path
'C:\\Users\\Samit\\Documents\\Spells'
>>> print(path)
C:\Users\Samit\Documents\Spells
>>> data = r"John's price \n to \\day of /\"
SyntaxError: EOL while scanning string literal
>>> print(data)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(data)
NameError: name 'data' is not defined
>>> s = 'parrot'
>>> print(s[3])
r
>>> type(s[4])
<class 'str'>
>>> c = 'oslo'
>>> c.capitalize()
'Oslo'
>>> c.count()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.count()
TypeError: count() takes at least 1 argument (0 given)
>>> c.lower()
'oslo'
>>> 'สวัสดีนี่คือ python นั่นเอง
SyntaxError: EOL while scanning string literal
>>> 'สวัสดีนี่คือ python นั่นเอง'
'สวัสดีนี่คือ python นั่นเอง'
>>> 'สวัสดีนี่คือ python นั่นเอง s\u00e5 for h\u00f8re'
'สวัสดีนี่คือ python นั่นเอง så for høre'
>>> '\xe5'
'å'
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
