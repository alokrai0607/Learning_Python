class Gorabazar :
   Gora = "Welcome to Gorabazar"
class Mahuabagh :
    Mahua = "Welcome to Mahuabagh"
class Ghazipur (Gorabazar,Mahuabagh):
    Ghazi = "Welcome to Ghazipur"

newplace = Ghazipur()

print(newplace.Gora)
print(newplace.Mahua)
print(newplace.Ghazi)

