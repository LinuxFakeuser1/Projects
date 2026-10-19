# third problem

"""
Description: The program receives a phrase in the variable palindrome and
determines whether it is a palindrome, meaning it reads the same from left to
right and from right to left. It ignores spaces and differences between
uppercase and lowercase letters. It also displays the normalized version
of the phrase (palin_mes).

Inputs:
- palindrome (string): phrase entered by the user with input().

Outputs:
- "Is palindrome: true" or "Is palindrome: false" (from result)
- "Normalized: <palin_mes>" (phrase in lowercase and without spaces)
- Error message if the input fails the validations.

Validations:
- palin_scan (palindrome.strip().lower()) must not be empty.
- palin_mes (palin_scan without spaces) must have at least 3 characters.

Test cases:
1) Normal: palindrome = "Anita lava la tina"
   -> palin_mes = "anitalavalatina"
      palin_check = "anitalavalatina"
      Is palindrome: true
      Normalized: anitalavalatina

2) Border: palindrome = "Ana" (exactly 3 characters)
   -> palin_mes = "ana"
      palin_check = "ana"
      Is palindrome: true
      Normalized: ana

3) Error: palindrome = "   " (only spaces)
   -> Error: the phrase cannot be empty.

   Another error case: palindrome = "a"
   -> Error: the phrase must have at least 3 characters (not counting spaces).
"""
# input the palindrome
palindrome = input("enter palindrome ")

# clean the string
 
palin_scan = palindrome.strip().lower()

# Palindrome test
palin_mes = palin_scan.replace(" ","").lower()
palin_count = len(palin_mes) >= 3
if palin_count == False:
    print("Error, empty string")
else:
    palin_check = palin_mes[::-1]
    check_result = palin_mes == palin_check
    result = check_result and palin_count
    print(palin_mes)
    print(palin_check)
    print(f"this palindrome is: {result}")


