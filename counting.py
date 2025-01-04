def countcharactertype(s):
    vowels = 0
    consonants = 0
    specialchar = 0
    digit = 0
    
    # Iterate through the string
    for i in range(0, len(s)):
        ch = s[i]
        
        # Check if the character is alphabetic and convert to lowercase if necessary
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            ch = ch.lower()  # Convert to lowercase for easier vowel check
            
            # Check if the character is a vowel
            if ch in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        
        # Check if the character is a digit
        elif ch >= '0' and ch <= '9':
            digit += 1
        
        # Otherwise, it's a special character
        else:
            specialchar += 1
    
    # Print the results
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digit)
    print("Special characters:", specialchar)

# Input string from user
str_input = input("Enter a string: ")
countcharactertype(str_input)
