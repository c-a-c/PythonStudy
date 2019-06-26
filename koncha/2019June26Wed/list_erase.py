integer = [1,2,3,4,5,6,7,8,9,]

#Popを使用
# integerリストの要素を全てコピー(別のリストを作成)
#.copyがないと名前は違うが同じものになってしまう
poped_list = integer.copy()

poped_list.pop(1)
print(poped_list)

# Eraseを使用
removed_list = integer.copy()

removed_list.remove(1)
print(removed_list)

if poped_list is integer:
    print("Yes")
else:
    print("No")
