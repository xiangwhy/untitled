__author__ = 'xiang_000'

file = r"d:\1.txt"
txt = open(file, 'r')

print("Here's your file %r:" % file)
print(txt.read())
txt.close()
print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)
txt.close()