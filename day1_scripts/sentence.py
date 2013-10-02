# step 1: get the list of arguments
import sys
newlist = sys.argv[1:]

# step 2: sort the list
newlist.sort()

# step 3: get the last word
lastword = newlist[-1]
allbutlast = newlist[0:-1]

# step 4: join the first two words with commas
newlist2 = ', '.join(allbutlast)

# step 5: add the 'and' and last word and full stop
newlist2 += ', and ' + lastword + '.'

# print the result
print(newlist2)

# can use the 'title' method to capitalise the first word
# or the 'capitalize' method
