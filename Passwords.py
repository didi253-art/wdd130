# Password Strength Project - CSE 111
# Enhancement: Includes robust UTF-8 file decoding and flexible case-sensitive top password checking.

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    """
    Reads a file line by line and checks if the word exists.
    Performs case-sensitive or case-insensitive matching based on parameters.
    """
    if not case_sensitive:
        word = word.lower()
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if not case_sensitive:
                    if file_word.lower() == word:
                        return True
                else:
                    if file_word == word:
                        return True
    except FileNotFoundError:
        pass
    
    return False


def word_has_character(word, character_list):
    """
    Loops through each character in the word to see if any 
    character is present in character_list.
    """
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """
    Calculates a numeric complexity value from 0 to 4 based 
    on the types of characters contained in the word.
    """
    score = 0
    if word_has_character(word, LOWER):
        score += 1
    if word_has_character(word, UPPER):
        score += 1
    if word_has_character(word, DIGITS):
        score += 1
    if word_has_character(word, SPECIAL):
        score += 1
    return score


def password_strength(password, min_length=10, strong_length=16):
    """
    Evaluates password strength (0 to 5) based on length, 
    dictionary match, top password match, and character complexity.
    """
    # 1. Check dictionary words (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Check top passwords (case-sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Check minimum length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Check strong length (fixed to include 16 and above)
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. Complexity score calculation
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength


def main():
    print("--- Password Strength Checker ---")
    user_input = ""
    while user_input != "q" and user_input != "Q":
        user_input = input("Enter a password (or 'q' to quit): ")
        if user_input == "q" or user_input == "Q":
            break
        
        strength = password_strength(user_input)
        print(f"Calculated Password Strength: {strength}\n")


if __name__ == "__main__":
    main()
