'''If statement in List-comps
'''
# Example-1 -->

# players = ['messy', 'rolando', 'maradona', 'backham', 'zidane']

# player_m = [player for player in players if player.startswith('m')]
# name_length_6 = [player for player in players if len(player) > 5]
# print(player_m)
# print(name_length_6)

# Example-2 -->

# numbers = [3, 4, 5, 6, 78, 72, 39, 11, 13]

# divisible_by_3 = [num for num in numbers if num % 3 == 0]
# print(divisible_by_3)


###################
###################

'''Nested for-loops in List-comps
'''

# players = ['messy', 'rolando', 'maradona', 'backham', 'zidane']

# super_heros = ['spiderman', 'ironman', 'superman', 'thor', 'hulk']

# combinations = []
# for player in players:
#     for sup_hero in super_heros:
#         combinations.append((player, sup_hero))
# print(combinations)


# combinations = [(player, sup_hero)
#                 for player in players for sup_hero in super_heros]

# print(combinations)
