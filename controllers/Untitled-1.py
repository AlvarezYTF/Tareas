for i in range(5):
    a = ""
    for j in range(5 - i - 1):
        a += " "
    for j in range(2 * i + 1):
        a += "*"
    print(a)

for i in range(5-1):
    a = ""
    for j in range(2 * i + 1):
        a += " "
    for j in range(5 - i + 2):
        a += "*"
    print(a)

