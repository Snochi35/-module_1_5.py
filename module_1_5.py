#1
immutable_var = (1, 2, 'word', True)
#2
print(immutable_var)
print(type(immutable_var))
#3
# immutable_var[0] = 2
# нельзя заменить элемент в кортеже по индексу, так как кортеж хранит ссылку на список, а не сам список
mutable_list = [1, 2, 'world', True]
mutable_list[0] = 3
print(mutable_list)