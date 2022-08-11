with open("testk.txt", encoding="UTF-8") as f: 
    s = f.readlines()
n = int(input())
# print(s)
summma = 0
count = 0
for i in s: 
    for j in i:
        # print(j)
        if j == " " or j == "\n": 
            if count == n: 
                summma += 1
            count = 0
        else: 
            count += 1
print(summma)
        

