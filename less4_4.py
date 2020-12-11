list_1=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# [23, 1, 3, 10, 4, 11]
# list_2 = []
#  for i  in range(len(list_1)):
#      if (list_1.count(list_1[i]) == 1):
#          list_2.append(list_1[i])
#  print(list_2)
qwer = (el for el in list_1 if list_1.count(el) == 1)
print(list(qwer))