n=int(input())
s=[input() for _ in range(n)]
s.sort(key=lambda x:len(x))
print("".join(s))