integer = [1,2,3,4,5,6,7,8,9,]

# Popを使用
# integerリストの要素を全てコピー
poped_list = integer.copy()
# poped_list = integer

poped_list.pop(-8)
print(poped_list)
print(integer)

if poped_list is integer:
	print("Same")
else:
	print("No")

# Eraseを使用
removed_list = integer.copy()
# removed_list = integer

removed_list.remove(1)
print(removed_list)
print(integer)

if removed_list is integer:
	print("Same")
else:
	print("No")
