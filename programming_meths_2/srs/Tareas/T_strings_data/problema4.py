# Problema 4
"""
Problem 4: Sentence analyzer

Description: The program receives a sentence, removes leading and trailing
spaces, splits it into words, and shows the word count, the first and last
words, and the shortest and longest words by length.

Inputs:
- sentence (string): sentence entered by the user with input().

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
- Error message if the input fails the validations.

Validations:
- clean_sentence (sentence.strip()) must not be empty.
- words (clean_sentence.split()) must contain at least one word.

Test cases:
1 Normal: "  The quick brown fox  "
   -> Word count: 4
      First word: The
      Last word: fox
      Shortest word: The
      Longest word: quick

2 Border: "Hello" (a single word)
   -> Word count: 1
      First word: Hello
      Last word: Hello
      Shortest word: Hello
      Longest word: Hello

3 Error: "   " (only spaces)
   -> Error: the sentence cannot be empty.
"""
# input the sentence
sentence = input("Enter a sentence: ")

# clean the string
clean_sentence = sentence.strip()

# Validation 1: not empty
if clean_sentence == "":
    print("Error: the sentence cannot be empty.")
else:
    words = clean_sentence.split()

    # Validation process
    if len(words) == 0:
        print("Error: the sentence must contain at least one word.")
    else:
        shortest = words[0]
        longest = words[0]

        for word in words:
            if len(word) < len(shortest):
                shortest = word
            if len(word) > len(longest):
                longest = word

        print(f"Word count: {len(words)}")
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")