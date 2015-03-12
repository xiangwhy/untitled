import os

if os.fork():
    print('11111')
else:
    print('22222')