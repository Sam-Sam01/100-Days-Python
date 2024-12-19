import math

def number_of_cans(height, width, coverage):
    cans = math.ceil((height * width) / coverage)
    return cans

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
test_c = int(input("One can can cover: "))

print(f"Number of cans required: {number_of_cans(height=test_h, width=test_w, coverage=test_c)}")