m = ["antonie", "riziki", "shikanda", "geoffrey"]
n = int(len(m))
i = 0
for i in range(1, n+1):
    print(i)
    i += 1   

for i, name in enumerate(m, 1):
    print(i, name)
