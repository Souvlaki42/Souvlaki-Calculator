import os
import math

os.system('cls' if os.name == 'nt' else 'clear')
title = lambda: os.system('title Souvlaki Calculator')
title()
color = lambda: os.system('color 2')
color()
D = 0
a = 0
b = 0
c = 0
print("Welcome to Souvlaki Calculator!")
print("If you don't know how to use that calculator just give as math symbol the word 'help'")
method = input("Please give me the math symbol :\n")
if method == "help":
	print("To start calculating please select one of the options below and give the required input:")
	print("Please select '+' if you want to find the result of an addition in the form of 'x+y'")
	print("Please select '-' if you want to find the result of a subtraction in the form of 'x-y'")
	print("Please select '*' if you want to find the result of a proliferation in the form of 'x*y'")
	print("Please select '/' if you want to find the result of a division in the form of 'x/y'")
	print("Please select '%' if you want to find the division remainder of a division in the form of 'x/y'")
	print("Please select '√' if you want to find the square root of a number in the form of '√x'")
	print("Please select '^' if you want to find the result of a number in power of another number in form of 'x^y'")
	print("Please select '+x' if you want to find the result of a primary equation by addition in form of 'x+a=b'")
	print("Please select '-x' if you want to find the result of a primary equation by subtraction in form of 'x-a=b'")
	print("Please select '*x' if you want to find the result of a primary equation with multiplication in form of 'x*a=b'")
	print("Please select '/x' if you want to find the result of a primary equation by division in form of 'x/a=b'")
	print("Please select 'x^2' if you want to find the result of a quadric equation in form of 'ax^2+bx+c=0'")
	print("Please select '>/' if you want to find the maximum common divisor of two numbers a and b with a>b")
elif method == "+":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) + int(y)
	print("The result of " + x + " + " + y + " is: " + str(output))
elif method == "-":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) - int(y)
	print("The result of " + x + " - " + y + " is: " + str(output))
elif method == "*":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) * int(y)
	print("The result of " + x + " * " + y + " is: " + str(output))
elif method == "/":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) / int(y)
	print("The result of " + x + " / " + y + " is: " + str(output))
elif method == "%":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) % int(y)
	print("The division remainder of " + x + " / " + y + " is: " + str(output))
elif method == "√":
	x = input("Please give me the x:\n")
	output = math.sqrt(int(x))
	print("The square root of " + x + " is: " + str(output))
elif method == "^":
	x = input("Please give me the x:\n")
	y = input("Please give me the y:\n")
	output = int(x) ** int(y)
	print("The result of " + x + " ^ " + y + " is: " + str(output))
elif method == "x^2":
	a = int(input("Please give the a:\n"))
	b = int(input("Please give me the b:\n"))
	c = int(input("Please give me the c:\n"))
	D = b**2 - 4 * a * c
	print("D = " + str(D))
	if D > 0:
		out1 = ((-1 * b) + math.sqrt(D))/2*a
		out2 = ((-1 * b) - math.sqrt(D))/2*a
		print("The solutions of the quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")
		print("First solution is " + str(out1))
		print("Second solution is " + str(out2))
	elif D == 0:
		out = (-1 * b)/2*a
		print("The solution of the quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 is:")
		print("Only solution is " + str(out))
	else:
		print("The quadratic equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 has no solution in R")
elif method == "+x":
	a = int(input("Please give me the a:\n"))
	b = int(input("Please give me the b:\n"))
	out = b - a
	print("The solution of the primary equation x + " + a + " = " + b + " is: " + str(out))
elif method == "-x":
	a = int(input("Please give me the a:\n"))
	b = int(input("Please give me the b:\n"))
	out = b + a
	print("The solution of the primary equation x - " + a + " = " + b + " is: " + str(out))
elif method == "*x":
	a = int(input("Please give me the a:\n"))
	b = int(input("Please give me the b:\n"))
	out = b / a
	print("The solution of the primary equation x * " + a + " = " + b + " is: " + str(out))
elif method == "/x":
	a = int(input("Please give me the a:\n"))
	b = int(input("Please give me the b:\n"))
	out = b * a
	print("The solution of the primary equation x / " + a + " = " + b + " is: " + str(out))
elif method == ">/":
	a = int(input("Please give me the a:\n"))
	b = int(input("Please give me the b:\n"))
	if a>b:
		while b>0:
			c = a%b
			a = b
			b = c
		out = a
		print("The maximum common divisor of a and b with a>b is " + str(out))
	else:
		print("a has to be greater than b!")
else:
	print("This math solution isn't exist!")
pause = lambda: os.system('pause')
pause()