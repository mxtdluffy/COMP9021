# Written by Di Peng

'''
Prints out a conversion table of temperatures from Celsius degrees to Fahrenheit
degrees, with the former ranging from 0 to 100 in steps of 10.
'''

min_temperature = 0
max_temperature = 100
step = 10
# print a table
print('Celsius\tFahrenheit')
# the formula: 9/5C + 32 = F
for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = (int)(celsius * 9 / 5 + 32)
    print(f'{celsius:7}\t{fahrenheit:10}')
print('TEST 1 END')
