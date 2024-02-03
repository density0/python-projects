# 6-1
person = {'first': 'matt',
          'last': 'king',
          'age': 21}

# 6-2
fav_num = {'al': '7',
           'matt': '3',
           'jessica': '34',
           'zero': '0',
           'gabby': '135'}

print(fav_num)
print('-----------------------------')
# 6-3
glossary = {'tulpes': 'immutable list',
            'dicks': 'store data in a key-value pair',
            'list': 'stores a list of data, mutable',
            'OOP': 'structuring a program by giving it properties and behaviors to an object',
            'Functions': 'block of code which runs when its called'}

print(f"{glossary['dicks']}")

print("\n")
print('-----------------------------')
# 6-4
for word, define in glossary.items():
    print(f"{word}: {define}")
print('-----------------------------')
# 6-5
space = {'olympus mons': 'mars',
         'methane sea': 'titan',
         'dwarf': 'pluto'}
print("\n")
for char, planet in space.items():
    print(f"{char} is on the planet {planet}\n")

print('-----------------------------')
# 6-6
# list of planets
planets = ['earth', 'mars', 'venus', 'pluto', 'titan', 'saturn']

# looping through the list and finding planets that already in the dic
for planet in planets:
    if planet in space.values():
        print(f"theres already info on {planet}")
    else:
        print(f"surveying {planet} now...")

print('-----------------------------')
# 6-7
person2 = {'first': 'matt',
           'last': 'king',
           'age': 21}

person3 = {'first': 'crona',
           'last': 'lambrona',
           'age': 15}
people = [person, person2, person3]

for peeps in people:
    full_name = f"{peeps['first']} {peeps['last']}"
    age = f"{peeps['age']}"
    print(f"\n{full_name} is age {age}")
print('-----------------------------')
# 6-8
star0 = {'type': 'red dwarf',
         'size': 'small',
         'sequence': 'K4',
         'name': 'HB-213'}
star1 = {'type': 'red giant',
         'size': 'large',
         'sequence': 'M4',
         'name': 'Kiter-324'}
star2 = {'type': 'white dwarf',
         'size': 'super small',
         'sequence': 'A10',
         'name': 'Bass-39'}
galaxy = [star1, star2, star0]

for stars in galaxy:
    name = f"{stars['name']}"
    print(f"\n{name} is a {stars['size']} star, and its sequence is {stars['sequence']}")

# 6-9
fav_vacas = {'dorporpin': 'kibb',
             'vin-wf-33': 'yonce',
             'marmin': 'leon'}
print('-----------------------------')
for places, name in fav_vacas.items():
    print(f"{name} wanted to visit {places}\n")
print('-----------------------------')

# 6-10
fav_num = {'al': ['7', '34'],
           'matt': ['3', '322'],
           'jessica': ['34', '345'],
           'zero': ['0', '3523'],
           'gabby': ['135', '324324', '333']}

for name, num in fav_num.items():
    print(f"{name} fav numbers are: {num}")
print('-----------------------------')

# 6-11
Sectors = {
    'Cancri-A':
        {
            'Location System': 'Cancri',
            'Population': '70 billion',
            'fact': 'First penal system, this entire system sole purpose\n\t'
                    'is for punishment for capital crimes against our glorious empire'
        },
    'Wasp-232':
        {
            'Location System': 'REDACTED',
            'Population': '0',
            'fact': "This system is strictly forbidden from entering, idling, passing through"
                    ",\n\tsurveying, all attempts to discover this system and its planets inhabitants"
                    " \n\twill result in your transfer to our camps in Cancri on Cancri-B."
        },
    'Kepler 22B':
        {
            'Location System': 'Kepler',
            'Population': '300 billion',
            'fact': 'Paradise'
        }
}

for name, info in Sectors.items():
    location = f"System: {info['Location System']}\n\tPlanet:{name}\n\tPop: {info['Population']}"
    print(f"{location}\n\tfact: {info['fact']}")
print('-----------------------------')

# 6-12

