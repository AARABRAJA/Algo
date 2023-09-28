#Job 1.2
def draw_triangle(height):
    for i in range(height):
        if i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

# Exemple:
draw_triangle(5)