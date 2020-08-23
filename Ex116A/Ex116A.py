tramStop = int(input())
Passengers = list()
i = 0
CurrentPassenger = 0
maxPassenger = 0
while i < tramStop: 
    s= str(input())
    m = list(s.split(" ")) 
    Passengers.append(m)
    i += 1
for i in range(0, tramStop):
    CurrentPassenger = CurrentPassenger + int(Passengers[i][1]) - int(Passengers[i][0])
    if CurrentPassenger > maxPassenger:
        maxPassenger = CurrentPassenger
        
print(maxPassenger)