s = str(input())
n = list(s.split(" "))
Limak = int(n[0])
Bob = int(n[1])
i = 1
while True:
    if (Limak*3**i) <= (Bob*2**i):
        i += 1
    else:
        break

print (i)