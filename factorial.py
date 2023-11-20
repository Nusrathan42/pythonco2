def factorial(n):                                              
    if n==0:   
        return 1
    else:
        return n * factorial(n-1)
num=int(input("enter a number:"))
if num<0:
    print ("factorial is not defined foe negative numbers.")
elif num==00:
    print(f"{num}!=1")
else:
    fact=factorial(num)
    print(f"{num}!={fact}")
