#sivapriya a v
# november 19 2024
#python program to draw patters
limit=int(input("enter a number"))

for i in range(limit+1):
    for j in range(i):
        print("*",end="")
    print()


for i in range(limit,0,-1):
    for j in range(i):
        print("*",end="")
    print()


for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range((2*i)-1):
        print("*", end="")
    print()


for i in range(limit,0,-1):
    for j in range (limit-i):
        print(" ",end="")
    for k in range((2*i)-1):
        print("*",end="")
    print()





