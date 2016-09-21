#!/usr/bin/env python

"""
Jon Ernster
02/23/2016

Description: Read a file containing hive table names and 
generate the SQL to convert Hive RCFile tables to ORC tables

Usage:  python hive-orc-gen-sql.py tables.txt
"""

import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ Functions

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n"): return x[:-1]
    return x[:]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file = sys.argv[1]

f = open(file, 'r')

l = []
orc_ext = "_orc"

for line in f:
	#line = line.rstrip('\n')
	line = chomp(line)
	l.append(line)

f.close

for t in l:
	print "SELECT COUNT(*) FROM " + t + ";" 

for t in l:
	print "CREATE TABLE " + t + orc_ext + " LIKE " + t + ";"

for t in l:
	print "ALTER TABLE " + t + orc_ext + " SET FILEFORMAT ORC;"

for t in l:
	print "INSERT INTO TABLE " + t + orc_ext + " SELECT * FROM " + t + ";"

for t in l:
	print "SELECT COUNT(*) FROM " + t + orc_ext + ";"
