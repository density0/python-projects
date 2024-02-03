import json

preferences = {'Mode': 'Hard', 'Sensitivity': 56, 'Display Screen': 'FullScreen'}

filename = 'gaming.json'

# dump stores the data
with open(filename, 'w') as settings:
    json.dump(preferences, settings)


# load looks inside the file and reads the list back into memory
with open(filename) as modes:
    inside = json.load(modes)
print(inside)


