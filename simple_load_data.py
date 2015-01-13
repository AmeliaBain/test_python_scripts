# This program was written by Simon

# import the numerical python package
import numpy as np

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"
# my_data = np.loadtxt(fname = 'some_data.csv', delimiter=',')

f = open('some_data.csv','r')

print "What is f?"
print f

lines = f.readlines()

print "these are the lines in the file"
print lines

line = lines[0]

split_line = lines[0].split(',')
print "split line is: "
print split_line

for element in split_line:
  num = int(element)
  print num


