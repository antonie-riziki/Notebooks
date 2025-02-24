#Looping through different lists
real_name = ["Peter Parker", "Clerk Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universe = ["Asgard", "Washington", "Marvel", "DC"]

for real_name, heroes, universe in zip(heroes, real_name, universe):
    print(f"{real_name} is known as {heroes} from {universe}")
    
