#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_year_leap(year):
	if (year>=0):
		if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
			return 'Высокосный год'
		else:
			return 'Не высокосный год'
	else:
		return 'Введите положительное число'


if __name__ == "__main__":

	
	
	if len(sys.argv) == 2:
		try:
			a =int(sys.argv[1])
			print(is_year_leap(a))
		except ValueError:
			print('Некорректный ввод данных')
			exit(1)
	else:
		print('Введите только год')
		exit(1)
	