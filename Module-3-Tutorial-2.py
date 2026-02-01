array = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
k = 5

has_found: bool = False
for x in range(len(array)):
    if k == array[x]:
        has_found = True
        print(f"{k} is the index of {x}")
        break

if has_found == False:
    print(f"{k} is not the index of the list")