s = str(input())
n = list(s.split(" "))
banana = 0
dollars = int(n[1])
cost = int(n[0])
for i in range (1, int(n[2])+1):
    banana += i
borrow = banana*cost - dollars
if borrow > 0:
    print(borrow)
else:
    print(0)