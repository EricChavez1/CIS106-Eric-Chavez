# 1. 
num_items = int(input("Enter the number of items in the list: "))
my_list = []

for _ in range(num_items):
    item = int(input("Enter an integer: "))
    my_list.append(item)

print("Initial list:", my_list)




# 2. 
my_list.insert(1, 99)
print("List after inserting 99 at position 1:", my_list)

# 3. 
if 99 in my_list:
    index_of_99 = my_list.index(99)
    my_list[index_of_99] = 100
print("List after replacing 99 with 100:", my_list)

# 4. 
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
my_list.extend(second_list)
print("First list after extending with second list:", my_list)


# 5. 
if 800 in my_list:
    my_list.remove(800)
print("First list after removing 800:", my_list)

# 6. 
if len(my_list) > 2:
    my_list.pop(2)
print("First list after removing the third item:", my_list)




# 7. 
grades = ["A", "B", "C", "A", "A", "C"]

# 8. 
count_A = grades.count("A")
print("Number of A grades:", count_A)

# 9. 
if "B" in grades:
    index_B = grades.index("B")
    print("Index of first B grade:", index_B)

# 10. 
if "F" not in grades:
    print("Grade F is not in the list.")

# 11. 
second_list.clear()
print("Second list after clearing:", second_list)

# 12. 
del second_list
try:
    print("Second list after deletion:", second_list)
except NameError:
    print("Second list no longer exists.")

# 13. 
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]


# 14. 
players.sort()
print("Sorted list of players:", players)



# 15. 
players2 = players.copy()
print("Copy of players list (players2):", players2)



# 16. 
players2.reverse()
print("Original players list:", players)
print("Reversed players2 list:", players2)
