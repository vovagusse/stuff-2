with open('smash mouth all star lyrics.txt', encoding="utf8") as f:
    lyrics = f.read()

lyrics_list = []
banned = [' ', ".", ',', '!', '?' ';', ':', '(', ')']
lyrics_word = ''
for w in lyrics:
    w = w.lower()
    if w == '\n':
        if lyrics_word != '':
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif w not in banned:
        lyrics_word += w
    else:
        if lyrics_word != '':
            lyrics_list.append(lyrics_word)
        lyrics_word = ''
if lyrics_word != '':
    lyrics_list.append(lyrics_word)
    lyrics_word = ''




check_dupes = {}

for w in lyrics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else:
        check_dupes[w] += 1

print(check_dupes)

most_freq_word = max(check_dupes.values())

for key in check_dupes.keys():
    if check_dupes[key] == most_freq_word:
        most_freq_word = key, check_dupes[key]
        break

print(f'Most frequent word in this song is {most_freq_word[0]} - {most_freq_word[1]} times repeated')