from pathlib import Path
import json

adjectives = []
nouns = []

files = [x for x in Path.cwd().iterdir() if x.suffix == '.json']

for file in files:
    with open(file) as f:
        data = json.loads(f.read())
        adjectives += [w.lower() for w, m in data.items()
                       if 'Adjective' in [
                           x for sl in m['MEANINGS'].values() for x in sl]]
        nouns += [w.lower() for w, m in data.items()
                  if 'Noun' in [
                      x for sl in m['MEANINGS'].values() for x in sl]]
dump = {
    'adjectives': adjectives,
    'nouns': nouns,
}

with open('word-data.json', 'w') as f:
    json.dump(dump, f)
