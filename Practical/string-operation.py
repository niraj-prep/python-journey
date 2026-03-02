st = input("Enter a string: ")
print("a) Total number of characters:",len(st))
print("b) String repeated 10 times:",st*10)

if len(st)==0:
	print("c) First character: String too short")
else:
	print("c) First character:",st[0])

if len(st)<3:
	print("d) First three characters: String too short")
else:
	print("d) First three characters:",st[:3])

if len(st)<3:
	print("e) Last three characters: String too short")
else:
	print("e) Last three characters:",st[-3:])
print("f) String backwards:",st[::-1])

if len(st)<7:
	print("g) Seventh character: String not long enough for seventh character")
else:
	print("g) Seventh character:",st[6])

if len(st)<2:
	print("h) String with first and last characters removed: String too short to remove characters")
else:
	print("h) String with first and last characters removed:",st[1:-1])


print("i) String in all caps:",st.upper())
print("j) String with every 'a' replaced with 'e':",st.replace('a','e'))
