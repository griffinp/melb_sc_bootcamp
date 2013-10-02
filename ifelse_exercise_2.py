import sys
input_number = int(sys.argv[1])
if input_number < 50 and input_number > 0:
    print("Minor")
elif input_number >= 50 and input_number < 1000:
    print("Major")
elif input_number < 0:
    print("Negative Number")
else:
    print("Severe")
