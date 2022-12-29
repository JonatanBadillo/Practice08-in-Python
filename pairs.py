'''
Develop a program that shows on screen all the pair number between 1-100
'''

for i in range (1,101):
    residue = i%2
    if residue == 0:
        print(f"{i} ")
