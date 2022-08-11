with open("0976.txt") as f: 
    s = f.readline() 
# s = "BEBRABEGBEBRABEBRABEazxcvbnmdfghjkl"
alp = "CDEFG*"
count = 0
maxc = 0
minc = 999999
kolvo = 0
adding = 0
flag = True
scoreflag = True
s = s.replace("BEBRA", "*")
# print(s)
for i in range(len(s)-4):
    if s[i] == "*":
        count += 5 
        if flag:
            kolvo += 1
            flag = False
    else:
        if s[i] == "B": 
            count += 1
            adding = 1
            if s[i+1] == "E": 
                count += 1
                adding = 2
                if s[i+2] == "B": 
                    count += 1
                    adding = 3
                    if s[i+3] == "R": 
                        count += 1
                        adding = 4
                        if s[i+4] == "A": 
                            count += 1
                            adding = 5
        flag = True
        for j in alp:      #концов очка
            if s[i+adding] == j:
                scoreflag = False 
        if scoreflag: 
            maxc = max(maxc, count)
            if count != 0:
                minc = min(minc, count)
        adding = 0 
        count = 0
        scoreflag = True
print(maxc,minc, kolvo )
                


            

