n = int(input("Number?"))
left = 1
right = n

while left <= right:
    print(left)

    if left != right:
        print(right)

    left += 1
    right -= 1
