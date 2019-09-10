#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_year_leap(year):
	if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
		return 'Высокосный год'
	else:
		return 'Не высокосный год'


if __name__ == "__main__":

	for param in sys.argv:
		print (param)
	
	if len(sys.argv) != 2:
		print("Не введен год")
		exit(1)
	
	try:
		a =int(sys.argv[1])
		print(is_year_leap(a))
	except ValueError:
		print('Некорректный ввод данных')
		exit(1)
	