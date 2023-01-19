# PETS -  Removing all instances of Specific Values (cat) from a List (pets)

pets = ['dog', 'cat', 'dog', 'golfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)