cubes = {
    "red": 12,
    "blue": 13,
    "green": 14
}

possible_games = []

file = open("input.txt", "r")

while True:
    line = file.readline()
    if not line:
        break
    # trim line break from end of line
    if line[-1] == "\n":
        line = line[:-1]
    # set game number value
    x = line.index(":")
    game = int(line[5:x])
    # set game possible initially true
    game_possible = True
    # set list of turns
    sets = line[x+2:].split(";")
    
    for set in sets:
        set_list = set.split(",")
        print(set_list)
        set_dict = {}
        for set in set_list:
            set = set.strip().split(" ")
            print("printing set", set)
            set_dict[set[1]] = int(set[0])
        print(set_dict)
        for (cube, number) in set_dict.items():
            print(set_dict[cube])
            if set_dict[cube] > cubes[cube]:
                game_possible = False
                break
    if game_possible == True:
        possible_games.append(game)

print(possible_games)
print(len(possible_games))
print(sum(possible_games))




file.close()