def perceint(a, b):
    return a/100 * b

def sum(a,b):
    return a + b

def main():
    print("Main function")
    print(f"Sum of 2 and 5 is {sum(2,5)}")
    print(f"15% of 200 is {perceint(15, 200)}")

if __name__ == "__main__":
    main()