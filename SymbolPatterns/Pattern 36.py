n = 3
for x in range(n, 0, -1):
    for y in range(n - 1, 0, -1):
        for z in range(0, x):
            print("*", end=" ")
        print()