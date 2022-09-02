f = open("monsters_simple.txt", "r")
monsters_dict={}
for line in f:
    k, v = line.strip().split(',')
    monsters_dict[k.strip()] = v.strip()
f.close()

print("Monsters Dictionary!")
search = input("What monster would you like to search for? Search: ")
check = monsters_dict.get(search)
if check:
    print(monsters_dict[search])
else:
    print("Check your spelling. Your search was not found.")
