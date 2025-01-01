# input
N,X = map(int,input().split())
A = list(map(int,input().split()))
Answer = False

# 全探索
for i in range(N):
  if A[i] == X:
    Answer = True
    
# 出力
if Answer == True:
  print("Yes")
else:
  print("No")