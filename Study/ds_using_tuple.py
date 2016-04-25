# I would recomment always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explict is better than implicit.

zoo = ('python','elephant','peguin')

print 'Number of animals in the zoo is ', len(zoo)

new_zoo = 'monkey','camel', zoo

print '\n Number of cages int the new zoo is ', len(new_zoo)
print '\n All animals in the new zoo are', new_zoo
print '\n Animals brought from old zee are', new_zoo[2]
print '\n Last animals brought from old zoo is', new_zoo[2][2]
print '\n Number of animails in the new zoo is', len(new_zoo) -1+ len(new_zoo[2])