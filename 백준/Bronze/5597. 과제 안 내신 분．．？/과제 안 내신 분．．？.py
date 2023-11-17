baskets = [i+1 for i in range(30)] 
arr = []
for _ in range(28):
    arr.append(int(input()))
arr.sort()
for i in baskets:
    if i not in arr:
      print(i)