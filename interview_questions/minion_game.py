def minion_game(string):
    vowels = "AEIOU"
    length = len(string)
    kevin_score = 0
    stuart_score = 0

    for i in range(length):
        if string[i] in vowels:
            # If the current letter is a vowel, Kevin gets points for all substrings starting from that letter
            kevin_score += length - i
        else:
            # If the current letter is a consonant, Stuart gets points for all substrings starting from that letter
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Example usage
minion_game("BANANA")
