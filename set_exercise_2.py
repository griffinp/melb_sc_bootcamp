import sys
string1 = sys.argv[1]
string2 = sys.argv[2]
string1l = string1.lower()
string2l = string2.lower()
nonletter = set([',', ' ', '.'])
# instead, could have used
# import string
# alphabet = string.lowercase
# ('lowercase' is a method in 'string', which was just imported)
# letters = charset1.intersection(alphabet)
charset1 = set(string1l).difference(nonletter)
charset2 = set(string2l).difference(nonletter)
inters = charset1.intersection(charset2)
print(len(inters))
print(inters)
print "First sentence: ", len(charset1.difference(charset2)), "unique characters"
print(charset1.difference(charset2))
print "Second sentence: ", len(charset2.difference(charset1)), "unique characters"
print(charset2.difference(charset1))
