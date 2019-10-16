x = range (1,100)
for y in x:
    if y % 3 == 0 and y % 5 == 0:
        print("FizzBuzz")
    elif y % 5 == 0:
        print("Fizz")
    elif y % 3 == 0:
        print("Buzz")
    else:
        print(y)
