n=int(input())

ans=[["."]*n for _ in range(n)]
for i in range(n):
  j=n-i-1
  if j>=i:
    for x in range(i,j+1):
      for y in range(i,j+1):
        if i%2==0:
          ans[x][y]="#"
        else:
          ans[x][y]="."
for a in ans:
  print("".join(a))