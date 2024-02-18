# Aprendiendo que son los sets en python

# Los sets son conjuntos
# Se pueden modificar
# No tienen orden
# NO se permiten duplicados

set_countries = {'col','mex','bol'} # Sintaxis para los sets
print(set_countries)
print(type(set_countries))

set_number = {2,1,56,3,2,3} # Todos los que se repitan serán ignorados
print(set_number)

set_types = {1,'hola',False,12.12}
print(set_types)

set_from_string = set('hola') # Making a set from a string.
print(set_from_string)
print(type(set_from_string))

set_from_tuples = set(('abc','cbv','as','abc')) # Making a set form a touple
print(set_from_tuples)

number = [1,2,3,4,4,4,5,6] # List
set_from_list = set(number) # Only will take the unique number and the rest wont appear.
print(set_from_list)
unique_number = list(set_from_list) # From a ser to a list.
print(unique_number) 