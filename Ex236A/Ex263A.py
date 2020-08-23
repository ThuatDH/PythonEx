"""
Bai toan:
Dau vao: ma tran 5x5 gom 24 so 0 va 1 so 1
Dau ra: So buoc can thiet de chuyen so 1 ve vi tri trung tam cua ma tran,
trong mot buoc chi duoc phep doi cho 2 hang hoac 2 cot cho nhau
Cach giai:
Tao mang 2 chieu nhan duoc tu ban phim
Tim vi tri cua so 1 trong mang 2 chieu 5x5, goi vi tri nay la hang i va cot j (i, j chay tu 0 -> 4)
So buoc can thiet = |i-2|+ |j-2|
"""
n = list()
i = 0
while i < 5: 
    s= str(input())
    m = list(s.split(" ")) 
    n.append(m)
    i += 1
for i in range (0,5):
    for j in range (0, 5):
        if n[i][j] == "1":
            print(abs(2-j)+ abs(2-i))