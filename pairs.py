'''
Develop a program that shows on screen all the number pairs between 1-100
'''

for i in range (1,101):
    residue = i%2
    if residue == 0:
        print(f"{i} ")