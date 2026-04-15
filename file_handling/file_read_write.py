# simple file handling (write, append, read)

# write (creates new file or overwrites)
with open("sample.txt", "w") as f:
    f.write("Hello\n")

# append (adds new line)
with open("sample.txt", "a") as f:
    f.write("How are you?\n")

# read (print content)
with open("sample.txt", "r") as f:
    print(f.read())
