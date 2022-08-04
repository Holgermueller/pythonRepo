print("Write something to the file:")
line = input(": ")
with open("record.txt", "a") as f:
    f.write(line)
    f.write('\n')
