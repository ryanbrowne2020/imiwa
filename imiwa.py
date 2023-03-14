

import json
import csv

with open('Favourites.imixch', 'r') as file:
    jfile = json.load(file)

f = open('Japanese.tsv', 'w', encoding="utf-8")
writer = csv.writer(f, delimiter='\t', lineterminator='\n')

for entry in jfile['lists'][0]['list']['items']:
    if entry['kanji']:
        kanji = entry['kanji'][0]
    else:
        kanji = []
    readings = entry['reading'][0]
    meanings = entry['meaning']['eng']
    row = []
    row.append(kanji)
    row.append(readings)
    row.append(meanings)
    writer.writerow(row)

f.close()


