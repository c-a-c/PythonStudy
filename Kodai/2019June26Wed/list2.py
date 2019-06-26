int_str = [1, "2", 3, "4", 5, "6", 7, "8", 9, ]

print("Get One Element")
#int = "str"
for i in int_str:
    print(i, type(i))
    if(type(i) == int):
        print("数字")
print()
