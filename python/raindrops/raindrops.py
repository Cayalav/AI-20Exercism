def convert(number):
    rainDrops = ''
    if (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
        return str(number)      
    if number % 3 == 0:
        rainDrops += 'Pling'
    if number % 5 == 0:
        rainDrops += 'Plang'
    if number % 7 == 0:
        rainDrops += 'Plong'
    return rainDrops