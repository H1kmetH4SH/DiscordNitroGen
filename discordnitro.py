import random
import string
a=int(input("How many codes do you want to generate : "))
alphabet=list(string.ascii_letters)
numbers=["1","2","3","4","5","6","7","8","9","0"]

for i in range(a):
    code=[]
    
    for i in range(12):
        Na_selection=random.randint(0,1)
        if Na_selection==0:
            selection=random.randint(0,len(alphabet)-1)
            code.append(alphabet[selection])
        else:
            selection=random.randint(0,len(numbers)-1)
            code.append(numbers[selection])
    

    print(f'https://discord.gift/{"".join(code)}')