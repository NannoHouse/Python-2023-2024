def number_of_vowels(text):
    count = 0
    for char  in text:
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
            count += 1
        
        print(char.lower())
            
    return count



print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)
