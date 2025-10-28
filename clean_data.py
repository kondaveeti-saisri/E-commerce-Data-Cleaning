# clean_data.py

# Ask the user to enter product IDs (separated by commas)
user_input = input("Enter product IDs separated by commas: ")

# Convert the input string into a list of integers
product_ids = [int(x.strip()) for x in user_input.split(",")]

print("\nOriginal product IDs:", product_ids)

# Remove duplicates using set()
unique_product_ids = list(set(product_ids))

# Sort for clean output
unique_product_ids.sort()

print("Cleaned product IDs:", unique_product_ids)
