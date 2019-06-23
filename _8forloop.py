Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ["apple","banana","cherry","mango"]
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
mango
>>> for x in "banana"
SyntaxError: invalid syntax
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> for x in "ยินดีต้อนรับสู่การเรียนไพทอน":
	print(x)

	
ย
ิ
น
ด
ี
ต
้
อ
น
ร
ั
บ
ส
ู
่
ก
า
ร
เ
ร
ี
ย
น
ไ
พ
ท
อ
น
>>> for x in fruits:
	print(x)
	if x == "banana":
		break

	
apple
banana
>>> for x in fruits:
	if x == "banana":
		break
	print(x)

	
apple
>>> x,y,z = "Orange","Banana","Cherry"
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> x=y=z = "Oragne"
>>> pirnt(x+y+z)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pirnt(x+y+z)
NameError: name 'pirnt' is not defined
>>> print(x+y+z)
OragneOragneOragne
>>> 
