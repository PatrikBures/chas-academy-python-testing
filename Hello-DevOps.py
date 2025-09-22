def get_int(a):
    while True:
        num = input(a)

        try:
            num = int(num)
        except:
            print("not an int")
            continue
        return int(num)


name = input("What is your name? ")

print(f"Hello {name}! input some ints.")

num1 = get_int("num1: ")
num2 = get_int("num2: ")

print(f"{num1} * {num2} = {num1 * num2}")

