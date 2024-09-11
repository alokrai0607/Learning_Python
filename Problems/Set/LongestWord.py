#Write a function that takes a list of words and returns the word with 
#the most unique characters. Use sets to determine uniqueness.

def word_with_most_unique_chars(sen):
    words = sen.split()
    maxunword = ""
    maxuniqco=0
    
    for w in words:
        uniqchars = set(w) 
        uniqcount = len(uniqchars)
        
        if uniqcount > maxuniqco:
            maxuniqco = uniqcount
            maxunword = w    
    return maxunword

sen = "Hello world how are you"
result = word_with_most_unique_chars(sen)
print(result)  # Output: "world"

