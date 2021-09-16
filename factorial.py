def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


user_fact = int(input("Enter the number whose factorial you want: "))
x = user_fact
fact = factorial(x)
print("The factorial of "+str(user_fact) +" is "+ str(fact))
