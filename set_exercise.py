import sys
string = sys.argv[1]
stringl = string.lower()
charset = set(stringl)
nonletter = set([',', ' ', '.'])
print(len(charset.difference(nonletter)))
# print(charset.difference(nonletter))

