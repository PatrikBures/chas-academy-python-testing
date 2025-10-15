size = 10
up = True
len = 1

while len > 0:
    print("*" * len)
    if up:
        len += 1
    else:
        len -= 1

    if len >= size:
        up = False
