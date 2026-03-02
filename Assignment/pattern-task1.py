n = 5

print("Pattern 1:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("\nPattern 2:")
for i in range(1, n+1):
    print(str(i) * i)

print("\nPattern 3:")
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPattern 4:")
for i in range(1, n+1):
    for j in range(i):
        print(1 if j % 2 == 0 else 0, end=" ")
    print()

print("\nPattern 5:")
num = 2
for i in range(1, n+1):
    for j in range(i):
        print(num, end="  ")
        num += 2
    print()

print("\nPattern 6:")
for i in range(1, n+1):
    print("*" * i)