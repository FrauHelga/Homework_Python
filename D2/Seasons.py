#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def season(number):
	if number > 0 and number < 13:
		if number == 1 or number == 2 or number == 12:
			return 'Winter'
		elif number == 3 or number == 4 or number == 5:
			return 'Sping'
		elif number == 6 or number == 7 or number == 8:
			return 'Summer'
		elif number == 9 or number == 10 or number == 11:
			return 'Autumn'
	else:
		print ('Введите число от 1 до 12')
		exit(1)

if __name__ == "__main__":
	
	if len(sys.argv) == 2:
		try:
			a =int(sys.argv[1])
			print(season(a))
		except ValueError:
			print('Некорректный ввод данных')
			exit(1)
	else:
		print('Введите только число')
		exit(1)