#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def arithmetic (x, y, operation):
	
	if (operation == '+'):
		return x+y
	elif (operation == '-'):
		return x-y
	elif (operation == '*'):
		return x*y
	elif (operation == '/'):
		try:
			return x/y
		except ZeroDivisionError:
			return "Деление на 0"
	else:
		return "Неизвестная операция"

if __name__ == "__main__":

	for param in sys.argv:
		print (param)
	
	if len(sys.argv) != 4:
		print("Недостаточно параметров")
		exit(1)
	
	try:
		a,b,op =float(sys.argv[1]), float(sys.argv[2]),sys.argv[3]
		print(arithmetic(a, b, op))
	except ValueError:
		print('Некорректный ввод данных')
		exit(1)
	