temperature=int(input("enter the temperature"))
scale=input("is this in (c)celcius or(f)fahrenheit")
if(scale=="c"):
    f=(9/5*temperature)+32
    print(temperature,"celcius is",f," fahrenheit ")
else:
    c=5/9*(temperature-32)
    print(temperature,"fahreheit is",c,"celcius")
