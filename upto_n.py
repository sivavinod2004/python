""""
author:abhirami
date:29-10-24
"""

limit=int(input("Enter the limit:"))
for number in range(2,(limit+1)):
    isPrime=True
    for i in range (2, (number//2)+1):
        if number%i==0:
            isPrime=False
            break
    if isPrime:
        print(number)