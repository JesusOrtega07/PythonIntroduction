# Modficando conjuntos

set_countries = {'col','mex','bol'} # Conjuto de prueba

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# Add
set_countries.add('pe') # We add the 'pe' to the set
print(set_countries) # Printing all the elements
set_countries.add('pe') # If we try to add it again, the element wont appear again
print(set_countries)

# Update
set_countries.update({'ar','ecua'})
print(set_countries)

# Remove 

set_countries.remove('col')
print(set_countries)
set_countries.discard('col')
#set_countries.remove('col') // If we try to remove a element who doesn't exist, the program will crash
print(set_countries)
set_countries.clear() # Removing all the elements in a set.
print(len(set_countries)) # Showing the lenght of the set

