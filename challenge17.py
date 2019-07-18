list = [5, 3, 7, 1, 8]

list.sort()
# only for lists
#sorts in ascending order
#mutates teh orginal list
#faster for lists because it does not make a copy unlike the other one
print(list)

#lista = ["a", "t", "b", "d", "c"]
# can sort other things as well, including lists
x = ('p', 'y','t' ,'h', 'o', 'n')
list1 = [1, 9, 7, 2, 6]
print(sorted(x))
print(sorted(list1))

print(sorted(x, reverse = True))
