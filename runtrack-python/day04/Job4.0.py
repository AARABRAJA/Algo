#Job 4.0
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact_res = factorial(n)
        print("The factorial of",n,"is:",fact_res)
    

main()
