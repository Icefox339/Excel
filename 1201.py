
def removeduplicates(l): 
    # список уже отсортирован
    removals = []
    for i in range(len(l)-1):
        if l[i] == l[i+1]: 
            # print(l[i])
            removals.append(l[i])
    remsum = 0
    for rem in removals: 
        if removals.count(rem) > 1: 
            l.remove(rem) 
            remsum += rem
        if removals.count(rem) == 1: 
            l.remove(rem)
            l.remove(rem)
            remsum += rem
            remsum += rem 
    return (l, remsum)

with open("1201.txt") as f: 
    n = f.readline() 
    l = list(map(int, f.readline().split(" ")))
summa = sum(l)
flag = True
defeat = True
if summa / 2 != int(summa/2): 
    print("NO")
    flag = False
podsum = int(summa / 2)
score = 0
if flag: 
    l.sort()
    lold = l.copy() # это ещё пригодится    
    # print(l)
    res = removeduplicates(l)
    # print(res)
    lnew  = res[0]
    podsum -= int(res[1]/2)
    # print(podsum)   
    while score <= podsum: # более-менее нормальная кринжатина
        if lnew == []:
            print("YES")
            defeat = False
            break
        for i in range(len(lnew)):
            score += lnew[i]
            if score == podsum: 
                print ("YES")
                defeat = False
                break
    if defeat:  #жуткая кринжатина
        podsum += int(res[1]/2)
        # print(podsum)
        # print(lold)
        for i in range(len(lold)):
            score = 0
            for j in range(i, len(lold)): 
                score += lold[j]
                if score == podsum: 
                    print("YES") 
                    defeat = False
        if defeat:
            print("NO")
    
        