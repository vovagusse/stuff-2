player_1 = {}

player_stats = {'Fireway': 'Amazon', 'Dewedor': 'Necromancer'}

for key in player_stats.values():
    print(key)

name = player_stats['Dewedor']

print(name)

player_stats['Dewedor'] = 'Alchemist'

player_stats['Vova_Gusse'] = 'High Gungeoneer'

print(player_stats['Vova_Gusse'])
print('not exists' in player_stats)
print('Fireway' not in player_stats)
