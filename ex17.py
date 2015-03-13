__author__ = 'xiang_000'

import os.path

form_file = r"d:\1.txt"
to_file = r"d:\2.txt"

print("Copying form %s to %s" % (form_file, to_file))

# We could do these two on one line too, how?

in_req = open(form_file, 'r')
in_data = in_req.read()

print("The input file is %d bytes long" % len(in_data))

print("Does the output file exist? %r" % os.path.exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(in_data)

print("Alright, all done.")

output.close()
in_req.close()

