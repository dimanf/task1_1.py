#!/usr/bin/python

def equal_elements(string):
	if isinstance(string, str):
		string_list = string.split()
		s = set()
		dublicate_list = []

		for string in string_list:
			if string not in s:
				s.add(string)
			else:
				dublicate_list.append(string)  
		return dublicate_list

	return "Parametr is not a string"

def list_statistic(l):
	if isinstance(l, (list, tuple)):
		statistic = {}
		for item in l:
			if not statistic.get(type(item).__name__):
				statistic[type(item).__name__] = 1
			else:
				statistic[type(item).__name__] += 1
		return statistic

	return "Parametr is not a list or tuple"

def last_char_sort(l):
	if isinstance(l, (list, tuple)):
		l.sort(key=lambda x: x[-1])
		return l

	return "Parametr is not a list or tuple"

def sorted_list(l, s):
	if isinstance(l, (list, tuple)) and isinstance(s, str):
		l.append(s)
		l.sort()
		return l

	return "Parametrs ont is a list or string"

def five():
	pass

def six(string):
	if isinstance(string, str):
		string_list = string.split()
		for i, s in enumerate(string_list):
			if len(s) % 2 != 0:
				string_list.pop(i)
		return string_list
	return "Parametr is not a string"

def seven():
	pass

# print equal_elements("Git will default to the more conservative Git will")

# print list_statistic(["Git will default", 123, "to the more", "conservative", {'dict': 123}, ['list', ]])

# print last_char_sort(['dub', 'red', 'frutella', 'calc'])

print sorted_list(['alisa', 'boris', 'clarc', 'roman'], 'anton')

# print six("Git will default to the more conservative")