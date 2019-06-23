Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> # Check keyword
>>> p = keyword.iskeyword("python")
>>> print(p)
False
>>> print(keyword.iskeyword("and"))
True
>>> x = 10; y = 20;
>>> z = x + y
>>> print(z)
30
>>> #---------------------------------
>>> # สร้างโดย นายก ขอคองอ
>>> # เมื่อ 1 jan 2019
>>> # ไม่สงวนสิทธิ์
>>> # --------------------------------
>>> """
คำอธิบายหลายบรรทัด
ได้อย่างต่อเนื่อง
จนจบคำสั่งตรงนี้
"""
'\nคำอธิบายหลายบรรทัด\nได้อย่างต่อเนื่อง\nจนจบคำสั่งตรงนี้\n'
>>> 
