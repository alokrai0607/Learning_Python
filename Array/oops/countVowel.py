def countVowel(input_string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    for char in input_string:
        if char in vowels:
            vowels_count += 1
    return vowels_count

myStr = "Alok Kumar Rai"
res = countVowel(myStr)
print("Number of vowels in the string : ",res)