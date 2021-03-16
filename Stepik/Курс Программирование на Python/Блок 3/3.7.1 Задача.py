numb_games = int(input('Введите количество игр: '))
game = []
teams = set()
for element in range(numb_games):
    game.append(input().split(';'))
for element in game:
    for goal in range(1, 4, 2):
        element[goal] = int(element[goal])
    for tm in range(0, 3, 2):
        teams.add(element[tm])
teams = list(teams)
d, win, drow, lose = {}, [], [], []
for team in game:
    if team[1] > team[3]:
        win.append(team[0])
        lose.append(team[2])
    elif team[1] < team[3]:
        win.append(team[2])
        lose.append(team[0])
    else:
        drow.append(team[0])
        drow.append(team[2])
for team in teams:
    d[team] = win.count(team) * 3 + drow.count(team)
teams = list(d.items())
teams.sort(key=lambda i: i[1], reverse=True)
for i in teams:
    print(i[0] + ':', win.count(i[0]) + drow.count(i[0]) + lose.count(i[0]), win.count(i[0]), drow.count(i[0]),
          lose.count(i[0]), i[1])
