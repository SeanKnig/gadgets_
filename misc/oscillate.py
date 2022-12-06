import string,random

def oscillate(size,lst):
    for char in range(size):
        if char < size//2:
            lst.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
            print(f'{char} : {lst}')

        if len(lst) == size//2:
            for x in range(len(lst)):
                for y in range(char):
                    if not len(lst) == 0:
                        lst.pop()
                        print(f'{char} : {lst}')
                        print(f'{char} : {lst}', file=open("outfun.txt", 'a'))
                    else:
                        continue

            if len(lst)==0:
                print('{}')
                oscillate(size-1,lst)

        if char==0 and not lst:
            exit(0)
        print(f'{char} : {lst}', file=open("outfun.txt", 'a'))
        #elif char == size//4:
        #    oscillate(size,lst)
lst=[]
for i in range(3):
    oscillate(32, lst)




#def oscillate(size,lst):
#    for char in range(size):
#        if char > size//2
