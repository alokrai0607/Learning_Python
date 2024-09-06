#strip() : Elemenate Extra space work like tream() function
word = input("Pass your first word: ").strip()
word2 = input("Pass your second word: ").strip()

# Remove spaces
# convert to lower case
word = word.replace(" ", "").lower()
word2 = word2.replace(" ", "").lower()
# first willl Check if the lengths are different
if len(word) != len(word2):
    print("Not Anagram")
else:
    if sorted(word) == sorted(word2):
        print("Anagram")
    else:
        print("Not Anagram")
