import re

a = re.findall('\d', 'abc123drf56')
b = re.findall('\d+', 'abc123drf56')
print(a)
print(b)
# ['1', '2', '3', '5', '6']
# ['123', '56']

print(re.match('a','ab')) # match
print(re.fullmatch('a', 'ab')) # none
print(re.match('a', 'ba')) # none
print(re.fullmatch('a', 'a')) # fullmatch

print(re.search('a', 'ba')) # search match

print(re.findall('aaa', 'aaaaa')) # ['aaa']
print(re.findall('aaa', 'aaaaaa')) # ['aaa', 'aaa']
# findall은 겹치는 것 허용 x

print(re.sub('a', 'z', 'ab'))

# 동일한 정규식을 여러번 사용하려면 compile
c = re.compile('a')
print(c.sub('zxc', 'abcdefg'))
print(c.sub('zxc', 'abcabcabc'))