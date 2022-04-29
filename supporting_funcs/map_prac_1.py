'''Map function example to convert a list of floats to int.
'''

from numpy import float_

float_list = [48.94361550016178, 93.86640165374581,
              79.89116959461286, 58.337087479349314,
              54.97249885280478, 20.304847374709876,
              33.79672039115971, 40.17853705562324]

int_list = list(map(lambda x: int(x), float_list))

print(int_list)
