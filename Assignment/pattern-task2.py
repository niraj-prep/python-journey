print("Pattern 1:")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPattern 2:")
for i in range(1, 6):
    for j in range(i):
        print("*" if j % 2 == 0 else "#", end=" ")
    print()

print("\nPattern 3:")
word = "python"
for i in range(len(word)):
    print(word[i] * (i + 1))

print("\nPattern 4:")
for i in range(1, len(word) + 1):
    print(word[:i])