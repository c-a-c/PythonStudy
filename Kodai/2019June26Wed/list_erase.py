integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
poped_list = integer.copy()
for i in integer:
    poped_list.append(1)
    print(i)


# Popを使用
# integerリストの要素を全てコピー
poped_list = integer.copy()
poped_list.pop(-9)
print(poped_list)

# Removeを使用
# .copy()を使用していないのでintegerの中身をそのまま変えている

if poped_list is integer:
    print("Same")


removed_list = integer  # .copy()
removed_list.remove(2)
print(removed_list)

poped_list.append(3)

print(removed_list)
