def product(l):
    result = 1
    for num in l:
        result = result * num
    return result

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
    except:
        print("not an int")
        continue

    current_num += 1
    numbers.append(num)

print(f"sum: {sum(numbers)}")
print(f"product: {product(numbers)}")
