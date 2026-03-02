import math

def add_numbers(a, b):
	return a+b

def area_of_circle(radius):

	area = math.pi*radius*radius
	return area
def reverse_string(s):

	return s[::-1]
def square_and_root(n):

	sq = n**2
	sqrt = math.sqrt(n)
	return sq, sqrt
def greet(name="User", greeting="Hello"):

	return f"{greeting}, {name}!"

a, b = map(int, input().split())
radius = float(input())
s = input()
num = int(input())
name_input = input()
greet_input = input()


print(f"Sum of {a} and {b} is:", add_numbers(a, b))
print(f"Area of circle with radius {radius} is:", round(area_of_circle(radius), 2))
print(f"Reverse of '{s}' is:", reverse_string(s))
sq, rt = square_and_root(num)
print(f"Square of {num} is {sq}, Square root is {round(rt, 2)}")
print(greet())  # Default
print(greet(name_input))
print(greet(name=name_input, greeting=greet_input))