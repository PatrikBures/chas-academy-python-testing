def try_int(num):
    try:
        int(num)
    except:
        return False
    return True

def get_int(a):
    while True:
        num = input(a)
        if try_int(num):
            return int(num)
        else:
            print("not an int")


name = input("What is your name? ")

print(f"Hello {name}! input some ints.")

num1 = get_int("num1: ")
num2 = get_int("num2: ")

print(f"{num1} * {num2} = {num1 * num2}")

