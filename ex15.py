# from the system import arg
from sys import argv

# set script and filename to be the output of argument-variable
script, filename = argv

# set txt to the opened file of argument-variables - words!
txt = open(filename)

# print out the file name and then the output of the words
print "Here's your file %r:" % filename
print txt.read()

# prompts user to enter the filename and then opens that file

print "Here's your file %r again!" % filename

#script, filename = argv

txt = open(filename)
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

print txt.read()

txt.close()
#  txt_again = open(file_again)

# # prints the file that the user wants printed
# print txt_again.read()