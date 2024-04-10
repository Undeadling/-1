immutable_var = (1, 2, 'a', 'b')
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(immutable_var)
print(mutable_list)
mutable_list[0] = 'c'
mutable_list[1] = 'd'
mutable_list[2] = '3'
mutable_list[3] = '4'
print (mutable_list)
#immutable_var[0] = 50 TypeError: 'tuple' object does not support item assignment
#print(immutable_var)
