def countOfUniqch(stri):
    ss = set()
    count = 0
    for i in stri:
        ss.add(i)
        a = len(ss)
    return a
        
print(countOfUniqch("Hello My Name is Alok and Yours ?"))