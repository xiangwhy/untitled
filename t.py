import os
import io
import json

file1 = open('d:\\json.txt', 'r')
a1 = file1.read()
print(file1.closed)
# a2 = json.dumps(a1)
a3 = json.loads(a1)
# print(a3[1])
file2 = open('d:\\1.txt','w')

for i in range(len(a3)):
    print(a3[i]['caption'] + '____价格:'+a3[i]['shop_price'])
    file2.writelines(a3[i]['caption'] + '____价格:'+a3[i]['shop_price']+'\n')
    print(i)

print(file2.closed)


    # print(a3[1]['caption'])

    print('fasf')
