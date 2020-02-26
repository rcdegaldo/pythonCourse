demo_list = [1, 2, 'hell', True, [1,2,3]]
colors = ['red', 'green', 'blue']
numbers_list = list((1, 2, 3, 4))
print(numbers_list)

rango = list(range(1,10))
print(len(rango))

print(demo_list[-1][2])

print('hell' in demo_list)

colors[1] = 'llelo'
colors.append('violet')
colors.extend(['white', 'black'])
colors.extend(('pink', 'orange'))
colors.insert(1, 'grey')

print(colors)

colors.pop(3)
colors.remove('black')
colors.sort(reverse=True)

print (colors)

print(colors.index('red'))