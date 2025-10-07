def product(i):
    result = 1
    for num in i:
        result = result * num
    return result

def main():
    name = input("What is your name? ")

    print(f"Hello {name}! input some ints.")

    numbers = []
    current_num = 0

    while True:
        num = input(f"num{current_num} (x to exit): ")
        
        if num == "x":
            break
        try:
            num = int(num)
        except ValueError:
            print("not an int")
            continue

        current_num += 1
        numbers.append(num)

    print(f"sum: {sum(numbers)}")
    print(f"product: {product(numbers)}")

if __name__ == "__main__":
    main()
