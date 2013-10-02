# longwinded way to get a string 20 characters long
# ending with spaces by expanding a tab
x = 'apple\t'
y = x.expandtabs(20-len('apple'))
print(y)

