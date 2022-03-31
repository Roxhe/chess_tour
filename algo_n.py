played_match = []
list_players = [1, 2, 3, 4, 5, 6, 7, 8]

list_players_h1 = list_players[:len(list_players) // 2]
list_players_h2 = list_players[len(list_players) // 2:]

score_all_player = {1: 0,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    6: 0,
                    7: 0,
                    8: 0}


def tour1():

    for i, j in zip(list_players_h1, list_players_h2):
        played_match.append((i, j))
        print(i, j)
        result = int(input("Qui est le gagnant ? (si égalité rentrez : 0) \n"))
        if result == 0:
            score_all_player[i] += 0.5
            score_all_player[j] += 0.5
        elif result == j:
            score_all_player[j] += 1
        elif result == i:
            score_all_player[i] += 1

    score_for_list = dict(sorted(score_all_player.items(), key=lambda x: x[1], reverse=True))
    list_players = list(score_for_list.keys())
    print("Fin Premier tour ")
    print("liste des matchs joués au tour 1:\n",played_match)
    print("classement :\n",score_all_player)
    print("liste des joueurs triée selon le classement :\n", list_players,
          "\n")


def type_match_de():
    played_match.append((list_players[i], list_players[i + 1]))

    print(list_players[i], list_players[i + 1])
    result = int(input("Qui est le gagnant ? (si égalité rentrez : 0) \n"))
    if result == 0:
        score_all_player[list_players_fm[i]] += 0.5
        score_all_player[list_players_fm[i + 1]] += 0.5
    elif result == list_players_fm[i + 1]:
        score_all_player[list_players_fm[i + 1]] += 1
    elif result == list_players_fm[i]:
        score_all_player[list_players_fm[i]] += 1

    list_players_fm.remove(list_players_fm[i])
    list_players_fm.remove(list_players_fm[i])


def type_match_e():
    played_match.append((list_players[i], list_players[i + 2]))
    print(list_players[i], list_players[i + 2])
    result = int(input("Qui est le gagnant ? (si égalité rentrez : 0) \n"))
    if result == 0:
        score_all_player[list_players_fm[i]] += 0.5
        score_all_player[list_players_fm[i + 2]] += 0.5
    elif result == list_players_fm[i + 2]:
        score_all_player[list_players_fm[i + 2]] += 1
    elif result == list_players_fm[i]:
        score_all_player[list_players_fm[i]] += 1

    list_players_fm.remove(list_players_fm[i])
    list_players_fm.remove(list_players_fm[i + 1])


tour1()

n = True
while n:
    list_players_fm = list_players
    print("Début Tour")

    for i in range(len(list_players_fm)):
        i = 0
        if len(list_players_fm) == 0:
            break
        if (list_players_fm[i], list_players_fm[i+1]) not in played_match:

            type_match_de()

        else:
            try:

                type_match_de()

            except IndexError:

                type_match_e()

    print("liste des joueurs restant après match :", list_players_fm)

    score_for_list = dict(sorted(score_all_player.items(), key=lambda x: x[1], reverse=True))
    list_players = list(score_for_list.keys())
    print("Fin Tour")
    print("score:\n", score_all_player)
    print("liste matchs joués:\n", played_match)
    print("classement des joueurs:", list_players)

    end_or_not = input("Continuer ? yes : y / no : n\n")
    if end_or_not == 'y':
        continue
    elif end_or_not == 'n':
        break
