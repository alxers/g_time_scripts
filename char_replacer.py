#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import pdb
import shutil

def convert_line(line):
	# { english: russian }
	dic = {
		'A': u'А',
		'B': u'В',
		'C': u'С',
		'E': u'Е',
		'H': u'Н',
		'K': u'К',
		'M': u'М',
		'O': u'О',
		'P': u'Р',
		'T': u'Т',
		'X': u'Х',
		'a': u'а',
		'c': u'с',
		'e': u'е',
		'o': u'о',
		'p': u'р',
		'x': u'х',
		'y': u'у'
	}
	line = line.decode('utf-8')
	for val in dic.keys():
		# pdb.set_trace()
		line = line.replace(dic[val], val)
	return line


with codecs.open('example_in.txt') as old, codecs.open('example_out.txt', 'w', 'utf-8') as new:
    for line in old:
        new.write(convert_line(line))

# shutil.move('output_h.txt', 'input_h.txt')
