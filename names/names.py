import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime before = 5.9769978523254395 seconds with 64 duplicates
# complexity = O(n^2)

'''

# solution using a Binary Search Tree == MY TRY #1
#

'''
# bst = BinarySearchTree('names')

# for name in names_1: # adds all names in names_1 to BST = O(n)
#     bst.insert(name)

# for name in names_2: # checks all names in names_2 to see if BST contains them = O(log n)
#     if bst.contains(name):
#         duplicates.append(name) # appends duplicates (BST.contains) to duplicates list

'''

# runtime after = 0.0990447998046875 seconds with 64 duplicates
# Complexity = O(nlog n)

'''

# stretch solution #1  ---STRETCH
# # define a dictionary 
# names_2_dict = {}

# # Confirm names are in the list
# for name in names_2:
#     names_2_dict[name] = True
# # Confirm name is in the list
# # and if it is in the name 2 dict
# # if so, append
# for name in names_1:
#     if name in names_2_dict:
#         duplicates.append(name)

# # runtime after = 0.007035255432128906 with 64 duplicates
# # Complexity = Linear O(n)

# using List comprehension MY TRY #2 ---Stretch
# duplicates = [n1 for n1 in names_1 for n2 in names_2 if n1 == n2]
    # run - time: 2.8079934120178223 seconds and 64 duplicates
# duplicates = [n2 for n2 in names_2 for n1 in names_1 if n2 == n1]
    # run - time:  2.479006052017212 seconds with 64 duplicates 
    # Complexity = O(n^2) not sure why list comprehension is faster than nested for loops
    
'''

# using set for both lists MY TRY #3 --Stretch 

'''
# iterate through both and compare the two
# & = compare. sets each bit to 1 if both bits are 1 use the & operator which is the union (duplicates) between the sets
# duplicates = set(names_1) & set(names_2)  ## this is the line to uncomment
    # run -time: 0.006998538970947266 seconds and 64 duplicates == slightly faster that stretch #1 (dict)
    # Complexity = O(n)
    


end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime was: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
