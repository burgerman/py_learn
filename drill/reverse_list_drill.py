my_list = ["a", "b", "c"]
print(list(reversed(my_list)))
print(my_list[::-1])


for element in sorted(my_list, reverse=True):
    print(element)