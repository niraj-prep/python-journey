# Prime Number Finder using while and for loop

a = int(input("Enter start number: "))
b = int(input("Enter end number  : "))

print(f"\nPrime numbers between {a} and {b}:")

n = a
while n <= b:
    if n < 2:
        n += 1
        continue
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
    n += 1
print()