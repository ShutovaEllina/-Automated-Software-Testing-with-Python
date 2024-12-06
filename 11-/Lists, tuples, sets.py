l = ["Bob", "Rolf", "Anne"]
# List of elements, add\remove. Order of elements
t = ("Bob", "Rolf", "Anne")
# tuple, can't add\remove. Order of elements
s = {"Bob", "Ralf", "Anne"}
# Set, add\remove, but no duplicate. No order

# print(l[2])

# l[0] = "Smith"
# print(l) # изменился порядок слов: ['Smith', 'Rolf', 'Anne']

# t[0] = "Smith" # error: tuple cannot be modified

#add element on the list
#l.append("Smith")
#print(l) # Вывод: ['Bob', 'Rolf', 'Anne', 'Smith']

# t.append("Smith")
# print(t) # Error: tuple, can't add\remove

# l.remove("Bob")
# print(l) # Вывод: ['Rolf', 'Anne']

# s.add("Smith")
# print(s) # Вывод: {'Anne', 'Smith', 'Ralf', 'Bob'}

# s.add("Smith")
# s.add("Smith")
# print(s) # Вывод: {'Anne', 'Smith', 'Ralf', 'Bob'}, не может быть дубликатов