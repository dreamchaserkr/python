# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
	print "Yes, the string starts with 'Swa' "

if 'a' in name :
	print "\nYes, it contains the string 'a' "

if name.find('war') != -1:
	print "\nYes, it contains the string 'war'"
	print "\n find : ", name.find('war')

if name.find('Swaa') != -1:
	print "\n find : ", name.find('Swaa')
else :
	print "\n find : ", name.find('Swaa')

delimiter = '__*__'
mylist = ['Brazil','Russia','India','China']

print "\n", delimiter.join(mylist)