def vowel_Const(n:str):
    if n.lower() in ("a","e","i","o","u") and n.upper() in ("A","E","I","O","U"):
        print(f"{n}"," : is Vowel")
    else:
        print(f"{n}"," : is Consonent")

vowel_Const("a")
vowel_Const("E")
vowel_Const("i")
vowel_Const("L")
vowel_Const("K")

