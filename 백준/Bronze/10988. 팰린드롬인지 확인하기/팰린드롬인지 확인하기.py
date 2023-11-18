Str = input()
Str = list(Str)
tmp = Str.copy()
Str.reverse()
if Str == tmp:
    print(1)
else:
    print(0)