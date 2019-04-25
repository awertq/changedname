''' bday date finder in the value of pi'''

with open("pi_value.txt") as pi:
    lines = pi.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

if "1996" in pi_string:
    print("bday found in line number")
else:
    print("not found")
