# Size 7 x 21
height7 = 7
width21 = height7 * 3

for stick_count in range(1, height7, 2):
    print(('.|.' * stick_count).center(width21, '-'))

print('WELCOME'.center(width21, '-'))

for stick_count in range(height7 - 2, 0, -2):
    print(('.|.' * stick_count).center(width21, '-'))

print('\n')
# Size 11 x 33
height11 = 11
width33 = height11 * 3

for stick_count in range(1, height11, 2):
    print(('.|.' * stick_count).center(width33, '-'))

print('WELCOME'.center(width33, '-'))

for stick_count in range(height11 - 2, 0, -2):
    print(('.|.' * stick_count).center(width33, '-'))
