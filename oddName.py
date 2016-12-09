__author__ = 'jc450453'
"""
"""
valid=False
while not valid:
    name=input("Enter your name:")
    if name != "" and not name.isspace():
        valid = True
        print(valid)

L=len(name)
for i in range(0,L,2):
    print(name[i])

