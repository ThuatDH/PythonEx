# Bai toan:
# Dau vao: nhap tu ban phim so n(1 ≤ n ≤ 50) va 1 chuoi co n ky tu
# Dau ra: Tim so lan nho nhat de loai bo ky tu sao cho chuoi nhap vao khong con 2 ky tu giong nhau nam canh nhau
# Cach giai:
# Doc chuoi co n ky tu vao tu ban phim, goi j la so lan phai loai bo ky tu
# Kiem tra tu ky tu dau tien den ky tu cuoi cung cua chuoi, neu 2 ky tu sat nhau giong nhau thi tang j len 1
# 
#
_len = int(input())
s = str(input())
j = 0
for i in range (0,_len-1):
    if s[i] == s[i+1]:
        j += 1
print(j)
