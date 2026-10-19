# problema 6

"""
Problem 6: Product label generator

Description: The program receives a product name and a price and builds a
one-line label with the format "Product: <NAME> | Price: $<PRICE>". The label
is adjusted to exactly 30 characters: it is padded with spaces if shorter and
cut if longer.

Inputs:
- product_name (string): product name entered by the user with input().
- price_value (string): price entered by the user with input(), converted to
  a number only to validate it.

Outputs:
- "Label: "<exactly 30 characters>"" (shown between quotes so the spaces
  are visible)
- Error message if the input fails the validations.

Validations:
- clean_name (product_name.strip()) must not be empty.
- price_value must be convertible to a positive number.

Test cases:
1) Normal: product_name = "Pen", price_value = "2.5"
   -> Label: "Product: Pen | Price: $2.5   "

2) Border: product_name = "Notebook", price_value = "15.99"
   (the base label is longer than 30 characters and gets cut)
   -> Label: "Product: Notebook | Price: $15."

3) Error: product_name = "   " (only spaces)
   -> Error: the product name cannot be empty.

   Another error case: product_name = "Pen", price_value = "-5"
   -> Error: the price must be a positive number.
"""

# input the product name and price
product_name = input("Enter product name: ")
price_value = input("Enter price: ")

# clean the strings
clean_name = product_name.strip()
clean_price = price_value.strip()

# Validation 1: name not empty
if clean_name == "":
    print("Error: the product name cannot be empty.")
else:
    # Validation 2: price must be a positive number
    try:
        price_number = float(clean_price)
    except ValueError:
        print("Error: the price must be a valid number.")
    else:
        if price_number <= 0:
            print("Error: the price must be a positive number.")
        else:
            # build the base label
            label = f"Product: {clean_name} | Price: ${clean_price}"

            # cut to 30 characters if longer
            label = label[:30]

            # pad with spaces at the end if shorter
            label = label + " " * (30 - len(label))

            print(f'Label: "{label}"')