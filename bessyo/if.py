var = 1

if var == 1 or var == 0:
    print("One")
    print("Indentation1")
    print("Indentation2")
elif var == 0:
    print("\"Zero\"")
    print("Indentation3")
    print("Indentation4")
else:
    print("Not \"One\"")
    print("Indentation5")
    print("Indentation6")

var = "str"
test = "s"

if test in var:
    print("Yes")
else: 
    print("No")

var = 5

var = 3 if var > 0 else 0
print(var)

