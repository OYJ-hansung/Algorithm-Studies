a = '123'
b = ['123456', '123123']
length = len(a)
if a in b[:length]:
    print('True')
    print(b[:length])
else:
    print('False')
    print(b[:length])