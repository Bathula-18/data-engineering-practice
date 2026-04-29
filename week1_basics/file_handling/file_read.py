# practice of reading a text file

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
