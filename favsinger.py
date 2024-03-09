from collections import Counter
nsong=int(input())
lsong=[]
lsong=list(map(int,input().split()[:nsong+1]))
counts = Counter(lsong)
x=[]
ns=nsong
if ns==1:
    print("1")
else:
    for element, count in counts.items():
        if count > 1:
            #here each element which is repeated is printed
            x.append(element)
    print(len(x))
    




