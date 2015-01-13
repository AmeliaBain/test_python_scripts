# This program was written by Simon M. Mudd
# A simple progrtam for reading csv files

# import the numerical python package
import numpy as np

print "Welcome to the load data file, I am your computer."
print "I am going to try to open the file some_data.csv"
# my_data = np.loadtxt(fname = 'some_data.csv', delimiter=',')

# here is where you tell python what the filename is
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


# find the number of elements in the line
n_elements_in_line = len(split_line)


# start an empty list. 
# what happens if you dont start with an empty list?
line_nums = []

# look through the line, getting the elements
for element in split_line:
  num = int(element)
  print num
  line_nums.append(num)
  
# the line numbers are:  
print line_nums