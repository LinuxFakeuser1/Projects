# problema 2

"""
Problem 2: <EmailVerificator>
Description: The program asks for an email address and checks that it has a
basic valid format: exactly one '@', at least one '.' after the '@', and no
spaces. If the email is valid, it also displays the domain.

Inputs:

emails = input("Enter your Email: ")

Outputs:


is a Valid Email and not valid email, prepare to die
if valid Email is true, also shows the "do_after_as"
variable

Validations:

- email_text must not be empty after strip().
- Exactly one '@' (count()).
- At least one '.' after the '@'.
- No spaces in the text.

Test cases:
1) Normal: "  user@gmail.com  "
   Output: Valid email: true / Domain: gmail.com
2) Border: "correofalso67@upv.edu.mx" (several dots in the domain)
   Output: Valid email: true / Domain: upv.edu.mx
3) Error: "user@@gmail" (two '@', no dot after it)
   Output: Valid email: false
"""
emails = input("Enter your Email: ")
# borrar espacios fuera del Email, para evitar fallos inecesarios
corrected_email = emails.strip()
# @ setting
AT_SIGN = "@"
DOT = "."
SPACES = " "
at_sign_present = corrected_email.find(AT_SIGN)
at_sign_cuantity = corrected_email.count(AT_SIGN)
#   Dots find
dot_position = corrected_email.find(DOT)
dot_after_as = corrected_email[at_sign_present+1:]
# Questioning
dot_is_present = at_sign_cuantity == 1
dot_position_questioning = DOT in dot_after_as
not_spaces = SPACES not in corrected_email
# Maquivelic if
if dot_is_present and dot_position_questioning and not_spaces:
    print(f"{dot_after_as} is a Valid Email")
else:
    print("not valid email, prepare to die")
# correofalso67@upv.edu.mx