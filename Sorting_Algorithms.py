# Assessment 3.7: Sorting Algorithms
# Name: Adrian Abendan Villarin
# Sorting Method: Bubble Sort

# Step 1: Store the full name.
full_name = "ADRIAN ABENDAN VILLARIN"

# Step 2: Create an array containing letters only.
# Spaces and symbols are excluded.
letters = [character for character in full_name.upper() if character.isalpha()]

# Step 3: Remove duplicate letters while keeping their original order.
unsorted_array = []
for letter in letters:
    if letter not in unsorted_array:
        unsorted_array.append(letter)

# Step 4: Copy the unsorted array so the original remains unchanged.
sorted_array = unsorted_array.copy()

# Step 5: Sort the array alphabetically using Bubble Sort.
for i in range(len(sorted_array) - 1):
    for j in range(len(sorted_array) - 1 - i):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = (
                sorted_array[j + 1],
                sorted_array[j]
            )

# Step 6: Display both arrays.
print("SORTING ALGORITHMS - BUBBLE SORT")
print("Full Name:", full_name)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
