Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if True:
	print("It's true!")

	
It's true!
>>> if False:
	print("It's true!")

	
>>> if bool("eggs"):
	print("Yes please!")

	
Yes please!
>>> if "eggs":
	print("Yes please!")

	
Yes please!
>>> h = 42
>>> if h > 50:
	print("Greater than 50")
else:
	print("50 or smaller")

	
50 or smaller
>>> if h > 50:
	print("Greater than 50")
    elif h < 20:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if h > 50:
	print("Greater than 50")
	elif h < 20:
		
SyntaxError: invalid syntax
>>> if h > 50:
	print("Greater than 50")
elif h < 20:
	print("Less than 20")
else:
	print("Between 20 and 50")

	
Between 20 and 50
>>> 
