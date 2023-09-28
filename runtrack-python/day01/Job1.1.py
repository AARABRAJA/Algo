#Job 1.1
def draw_rectangle(width, height):
    border = "|" + "-" * (width - 2) + "|\n"

    print(border + "|" + " " * (width - 2) + "|\n" * (height - 2) + border)

# Exemple:
draw_rectangle(10, 3)