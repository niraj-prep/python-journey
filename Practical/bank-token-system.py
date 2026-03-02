st = int(input())
et = int(input())
lt = []
print("Tokens from",st,"to",et)
for i in range(st,et+1):
	lt.append(i)
tup = tuple(lt)
even = tuple(i for i in tup if i%2==0)
odd = tuple(i for i in tup if i%2!=0)

print("EVEN_TUPLE:",even)
print("ODD_TUPLE:",odd)
s1 = even[::-1]
s2 = odd[::-1]
print("Reversed EVEN_TUPLE:",s1)
print("Reversed ODD_TUPLE:",s2)
s3=list(even[::-1])
s4=list(odd[::-1])
print("List from Reversed EVEN_TUPLE:",s3)
print("List from Reversed ODD_TUPLE:",s4)