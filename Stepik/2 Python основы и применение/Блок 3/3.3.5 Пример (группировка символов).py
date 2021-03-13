import re

pattern = r'(test)*'
string = 'testtest'
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 8), match='testtest'>

pattern = r'((abc)|(test|text)*)'
string = 'abc'
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 3), match='abc'>
print(match.groups())  # ('abc', 'abc', None)
print(match.group())  # abc

pattern = r'Hello (abc|test)'
string = 'Hello abc'
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 9), match='Hello abc'>
print(match.group())  # Hello abc
print(match.group(0))  # Hello abc
print(match.group(1))  # abc

pattern = r'(\w+)-\1'
string= 'test-test'
match =re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 9), match='test-test'>