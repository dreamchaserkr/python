import operator
# 'ab' is short for 'a'dress'b'ook

ab = {'Swaroop' : 'swaroop@swaroopch.com',
	'Larry' : 'larry@wall.org',
	'Matsumoto' : 'matz@ruby-lang.org',
	'Spammer' : 'spammer@hotmail.com'
	}

print 'All Dictionary list is : ', ab


sorted_ab = sorted(ab.iteritems(),key=operator.itemgetter(1), reverse= False)
print "\n All Dictionary list is : ", sorted_ab

#for name,address in sorted_ab.getitems() :
#	print format(name,address)


print "\n Swaroop's adresss is ", ab['Swaroop']

# Deleting a key-value pair
del ab['Spammer'] 

print "\n These are {} contacts in the address-book \n".format(len(ab))

for name,address in ab.items():
	print 'Contact {} at {}'.format(name,address)

#Adding a key-value pair

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print " \n Guido's address is ", ab['Guido']


nshoplist = ['apple','mango','caroot','banana']

print 'nShopList is 1 to -1 : ', nshoplist[1:-1]
print 'nShopList is 1 to 1 : ', nshoplist[1:1]
print 'nShopList is 1 to 2 : ', nshoplist[1:2]
print 'nShopList is 1 to end : ', nshoplist[1:]
