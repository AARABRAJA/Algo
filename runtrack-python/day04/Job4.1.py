#Job 4.1
def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    else:
        return x * power(x, n - 1)

def main():
        n = int(input("Enter the exponent n: "))
        x = float(input("Enter x: "))
        result = power(x, n)
        print(x,"^",n,"is:",result)
    
main()
