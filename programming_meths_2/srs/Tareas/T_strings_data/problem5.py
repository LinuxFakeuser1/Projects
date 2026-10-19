# problem 5 

"""
Description: The program classifies a password as weak, medium or strong
based on its length and the types of characters it contains (uppercase,
lowercase, digits and symbols). The rules are documented in the code comments.

Inputs:
- password_input (string): password entered by the user with input().

Outputs:
- "Password strength: weak", "Password strength: medium" or
  "Password strength: strong"
- Error message if the password is empty.

Validations:
- password_input must not be empty.
- Length is checked with len() (minimum 8 to be medium or strong).

Test cases:
1 Normal: "Hello123"
   -> Password strength: medium

2 Border: "Abc123!x" (exactly 8 characters, all four types)
   -> Password strength: strong

   Other border: "Abc123!" (7 characters)
   -> Password strength: weak

3 Error: "" (empty)
   -> Error: the password cannot be empty.
"""
# input the password
password_input = input("Enter password: ")

# Validation: not empty
if password_input == "":
    print("Error: the password cannot be empty.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    types_count = 0
    if has_upper:
        types_count += 1
    if has_lower:
        types_count += 1
    if has_digit:
        types_count += 1
    if has_symbol:
        types_count += 1

    if len(password_input) < 8 or types_count == 1:
        strength = "weak"
    elif types_count == 4:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")