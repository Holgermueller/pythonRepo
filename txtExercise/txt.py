print("Write something to the file:")
line = input(": ")
with open("txtExercise/record.txt", "a") as f:
    f.write(line)
    f.write('\n')
