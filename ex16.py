__author__ = 'xiang_000'

# file = input("文件路径")
print("Opening the file...")
file = r"d:\1.txt"
target = open(file, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.writelines("111111\n")
target.writelines("222222\n")
print("And finally, we close it.")
target.close()
