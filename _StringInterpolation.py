Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # String interpolation
>>> lang = 'Python'
>>> v = 3.7
>>> Str = f"I'm learing {lang} language in version {v}"
>>> print(Str)
I'm learing Python language in version 3.7
>>> Str2 = F"I'm learing {lang} language in version {v}"
>>> print(Str2)
I'm learing Python language in version 3.7
>>> 
>>> print('ภาษา {lang} เวอร์ชั่น {v}')
ภาษา {lang} เวอร์ชั่น {v}
>>> print(f'ภาษา {lang} เวอร์ชั่น {v}')
ภาษา Python เวอร์ชั่น 3.7
>>> 
