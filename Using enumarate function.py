name = ["antonie", "Geoffrey", "Daniel", "Wesley", "JohnPope"]

i = 0
for person in name:
    print(i, person)
    i += 1

print("======== RESTART: C:/Users/antonie/Desktop/Using enumarator function.py ========")
#alternatively

name = ["Naisula", "Shirlyne", "Joy Wanjima", "Saraphina", "Ashley Banks"]

for k, name in enumerate(name, start = 2):
    print(k, name)

print("======== RESTART: C:/Users/antonie/Desktop/Using enumarator function.py ========")
month = ["Jan", "Feb", "Mar" , "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for i, month in enumerate(month, start = 1):
    print(i, month)
