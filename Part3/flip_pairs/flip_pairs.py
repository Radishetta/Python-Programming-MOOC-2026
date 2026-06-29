n = int(input("Number?"))
pairs = []

for i in range(2, n + 1, 2):
    pairs.append([i, i - 1])

for pair in pairs:
    print(pair[0])
    print(pair[1])

if n % 2 != 0:
    print(n)
