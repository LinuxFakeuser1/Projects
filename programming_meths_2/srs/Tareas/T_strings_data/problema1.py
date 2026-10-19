## Problema 1 
""" 
Problem 1: <NameCorrector>
Description: 
The program prompts for a full name, removes leading and trailing spaces with strip(), and splits it into 
a list of words with split(), which also eliminates extra internal spaces. It then verifiesthat the list 
contains at least two words, as defined by the constant MINIMAL_WORDS, and raises a ValueErrorotherwise,
which also covers empty or whitespace-only input. If the input is valid, the words are joined and converted
to Title Case, a loop prints each word and builds the initials from their first letters, and the program
finally displays the formatted name and the initials (for example, “Alan Anguiano Ayala” and “A.A.A”).

Inputs:

full_name = <The name wanted to correct>

Outputs:

completed_name = <The name, fully corrected with propper typing, example: "Alan Anguiano Ayala"> 
initials = <The initials of the completed_name value, example: "A.A.A." as the initials of:
"alan anguiano ayala"

Validations:

- when there's no word in the input the the program automatically
  raises up the ValueError and ends the program
- If there are int values in the input the program also count
  that as no words, so it also triggers the ValueError 

Test cases:
Test cases:
1) Normal: 
   Input:    "alan anguiano ayala"
   Output:   Formatted name: Juan Carlos Tovar
             Initials: J.C.T.

2) Border: 
   Input:    "   MeXICAN     LOPEZ   "  (minimum of two words, mixed case, extra spaces)
   Output:   Formatted name: Mexican Lopez
             Initials: M.L.

3) Error: 
   Input:    "Pedro"  (only one word; "" or "     " also fail)
   Output:   ValueError: Error: not enough words, name and surname required
"""
full_name = input("Please, enter your name: ")
name_precleaned = full_name.strip()
name_cleaned = name_precleaned.split()
MINIMAL_WORDS = 2
minimal_words_check = name_cleaned
if len(minimal_words_check) < MINIMAL_WORDS:
    print("error, not enought words, name and surname required")
completed_name = " ".join(name_cleaned).title()
initials ="" 
for name_cleaned in completed_name.split():
    print(name_cleaned)
    initials += name_cleaned[0] + "."
print(f"your full name is {completed_name}")
print(f" initials: {initials}")
# AhuevoAlan