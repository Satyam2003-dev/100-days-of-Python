import math


def paint_calc(height, width, cover):
    area = height * width
    no_of_cans = math.ceil(area / cover)
    print(f"you'll need {no_of_cans} cans to paint the whole wall")

test_h = int(input("Enter the height of wall "))
test_w = int(input("Enter the width of wall "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

