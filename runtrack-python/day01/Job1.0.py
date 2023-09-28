#Job 1.0
for i in range(1, 101):
    # multaiple of 3 or 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # multiple of 3 
    elif i % 3 == 0:
        print("Fizz")
    
    # multiple of 3 or 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
