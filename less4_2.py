
list_1 =[11, 2, 5, 4, 8, 1, 3, 6, 452, 0, 3, 6]

def comparison (list):
    for i in range(len(list)-1):
        if list[i]< list[i+1]:
            yield list [i+1]

print(list(comparison(list_1)))