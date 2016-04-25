import sys

print "The command line arguments are : "
for i in sys.argv:
	print i

print "\n\n The PYThON_PATH is : ", sys.path, "\n"

help(int)