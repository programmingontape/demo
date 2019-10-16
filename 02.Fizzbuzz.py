def fizzbuzz(x):
    if (x %3==0) and (x%5==0):
        return"Fizzbuzz"
    if(x%5==0):
        return"Fizz"
    if (x %3==0):
        return "Buzz"
    return x
x = int(input("Enter value: "))
print(fizzbuzz(x))
