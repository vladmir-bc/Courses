number_of_commands = int(input())
commands = []
for command in range(number_of_commands):
    commands.append(input().split())
x = 0
y = 0
for element in commands:
    if element[0] == 'восток':
        x += int(element[1])
    elif element[0] == 'запад':
        x -= int(element[1])
    elif element[0] == 'север':
        y += int(element[1])
    else:
        y -= int(element[1])
print(x, y)
