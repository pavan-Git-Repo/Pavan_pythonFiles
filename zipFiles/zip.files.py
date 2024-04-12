mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

products = [a * b for a, b in zip(list1, list2)]
print(products)