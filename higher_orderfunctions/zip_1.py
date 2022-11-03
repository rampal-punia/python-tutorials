'''Zip function example: Zip two lists together.
'''
from numpy import int_


int_list = [1, 2, 3, 4, 5, 6]
superheros = ['spiderman', 'ironman', 'heman', 'flask', 'thor', 'antman']
powers = ['build webs', 'flying', 'extremely powerful', 'speed', 'lightening']
accuracies = [99.999, 99.999, 99.999, 99.999]

zipped_list = list(zip(int_list, superheros, powers, accuracies))
print(zipped_list)
