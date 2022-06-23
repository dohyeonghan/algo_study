# print(ord('d'))
data = input()
res = ''
for d in data:
    if d.isupper():
        if ord(d) + 13 > 90:
            check = ord(d) - 13
        else:
            check = ord(d) + 13
        res += chr(check)
    elif d.islower():
        if ord(d) + 13 > 122:
            check = ord(d) -13
        else:
            check = ord(d) + 13
        res += chr(check)
    else:
        res += d
print(res)