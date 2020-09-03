def subtr(a,b):
    return a - b

def squart(n):
    return n ** (1/2)

def perceint(a, b):
    """
    Parameters
    ----------
    a : number
        The percent
    b : number
        Of the amount you want
    """
    return a/100 * b

def div(a,b):
    return a / b

def sum(a,b):
    return a + b

def main():
    print("Main function")
    print(f"Sum of 2 and 5 is {sum(2,5)}")
    print(f"15% of 200 is {perceint(15, 200)}")
    print(f"Div of 10 by 5 is {div(10,5)}")
    print(f"Square root of 25 is {squart(25)}")
    print(f"3 minus 8 is {subtr(3,8)}")

if __name__ == "__main__":
    main()