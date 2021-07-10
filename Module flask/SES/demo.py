import pyperclip as pc
file = open("new.txt","r")
data=file.read()

a_file = open("new.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    
    list_of_lists.append(stripped_line)
print(str(list_of_lists))
pc.copy(str(list_of_lists))
a_file.close()