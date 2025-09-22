import sys

def try_int(num):
    try:
        int(num)
    except:
        print("not a int")
        sys.exit()
    return int(num)

name = input("What is your name? ")

print(f"Hello {name}!")

num1 = try_int(input("num1: "))
num2 = try_int(input("num2: "))

print(f"{num1} * {num2} = {num1 * num2}")

