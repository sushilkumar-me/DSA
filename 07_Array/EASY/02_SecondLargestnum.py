l = [10,10,10]
n = len(l)
lar = float("-inf")
slar= float("-inf")
for i in range(len(l)):
    if l[i] > lar: 
        lar = l[i]
    if l[i] > slar and l[i] < lar:
        slar = l[i]

if slar == float("-inf"):
    print("No second largest number")   
else:
    print(slar)  
