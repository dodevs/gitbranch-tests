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

if __name__ == "__main__":
    main()