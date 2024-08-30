
def table(n):
    store = ""
    for i in range(1,11):
        store += str(i*n)
    print(store)

print(table(5))

#Way-2
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {i * n}")
table(20)
