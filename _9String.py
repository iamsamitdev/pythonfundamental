Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # การประกาศตัวแปร String
>>> name = "Samit"
>>> site = 'samitkoyom.com'
>>> str1 = "This is my string"
>>> str2 = 'This is my string'
>>> # ความแตกต่างระหว่าง ' และ "
>>> sentent1 = "What's your name?"
>>> sentent2 = 'I\'m Samit'
>>> sentent3 = "He said \"I would learn Python first\"."
>>> sentent4 = 'His teach replied "Oh well!"'
>>> print(sentent1)
What's your name?
>>> print(sentent2)
I'm Samit
>>> print(sentent3)
He said "I would learn Python first".
>>> print(sentent4)
His teach replied "Oh well!"
>>> str = """\
HTTP response code
	200	Success
	404	Not found
	503	Service unavailable
"""
>>> print(str)
HTTP response code
	200	Success
	404	Not found
	503	Service unavailable

>>> firstname = 'Samit'
>>> lastname = 'Koyom'
>>> fullname = firstname+' '+lastname
>>> print(fullname)
Samit Koyom
>>> name = 'Johny' 'Doe'
>>> my_number = 'One '\
	    'Two '\n
SyntaxError: unexpected character after line continuation character
>>> my_number = 'One '\
	    'Two '\
	    'Three '
>>> print(name)
JohnyDoe
>>> print(my_number)
One Two Three 
>>> # Charterers of string
>>> s = 'Mountain'
>>> print(s[0])
M
>>> print(s[8])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(s[8])
IndexError: string index out of range
>>> print(s[7])
n
>>> s[2] = 'p'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s[2] = 'p'
TypeError: 'str' object does not support item assignment
>>> s1 = 'Mountain'
>>> print(s1[0:4])
Moun
>>> print(s1[4:6])
ta
>>> print(s1[0:2])
Mo
>>> s2 = 'marcuscode'
>>> print(s2[:6]) #marcus
marcus
>>> print(s2[6:]) #code
code
>>> # หาความยาวของ string
>>> s1 = 'Mountain'
>>> s2 = 'marcuscode'
>>> s3 = 'Python'
>>> print('length of s1 =', len(s1))
length of s1 = 8
>>> print('length of s2 =', len(s2))
length of s2 = 10
>>> print('length of s3 =', len(s3))
length of s3 = 6
>>> 
