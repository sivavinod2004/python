'''author:sivapriya a v
date:15-10-2024
to find factorial'''
number=int(input("enter a number:"))
factorial=1
while number>0:
    factorial=factorial*number
    number-=1
print(factorial)
